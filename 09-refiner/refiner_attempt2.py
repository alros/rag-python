import chromadb
from llama_index import ServiceContext, VectorStoreIndex, QueryBundle, get_response_synthesizer, PromptTemplate
from llama_index.callbacks import LlamaDebugHandler, CallbackManager, CBEventType
from llama_index.llms import Ollama
from llama_index.postprocessor import LLMRerank
from llama_index.prompts import PromptType
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.response.schema import RESPONSE_TYPE
from llama_index.response_synthesizers import ResponseMode
from llama_index.vector_stores import ChromaVectorStore

model = "mistral"
db_path = '../chroma_db/gutenberg'
kb_path = './kb'
db_collection = 'gutenberg'
retrieve_N_chunks = 5
reranker_top_n = 2


def query(prompt):
    db = chromadb.PersistentClient(path=db_path)
    chroma_collection = db.get_or_create_collection(db_collection)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    llm = Ollama(model=model)
    llama_debug = LlamaDebugHandler(print_trace_on_end=True)

    callback_manager = CallbackManager([llama_debug])

    service_context = ServiceContext.from_defaults(llm=llm,
                                                   embed_model="local",
                                                   callback_manager=callback_manager)

    vector_store_index = VectorStoreIndex.from_vector_store(vector_store,
                                                            service_context=service_context)
    vector_retriever_chunk = vector_store_index.as_retriever(similarity_top_k=retrieve_N_chunks)  # best N chunks

    query_engine = RetrieverQueryEngine.from_args(
        vector_retriever_chunk,
        service_context=service_context,
        verbose=True,
        response_mode=ResponseMode.COMPACT)

    query_bundle = QueryBundle(prompt)
    nodes = query_engine.retrieve(query_bundle)

    choice_select_prompt_text = (
        "A list of documents is shown below. Each document has a number next to it along "
        "with a summary of the document.\n\nGiven the following question: \n{query_str}\n\n"
        "Rank the documents by relevance. \n"
        "Example format: \n"
        "Document 1:\n<summary of document 1>\n\n"
        "Document 2:\n<summary of document 2>\n\n"
        "...\n\n"
        "Document 10:\n<summary of document 10>\n\n"
        "Question: <question>\n"
        "Answer:\n"
        "Doc: 9, Relevance: 7\n"
        "Doc: 3, Relevance: 4\n"
        "Doc: 7, Relevance: 3\n\n"
        "Let's try this now: \n\n"
        "{context_str}\n"
        "Answer:\n"
    )

    choice_select_prompt = PromptTemplate(
        choice_select_prompt_text, prompt_type=PromptType.CHOICE_SELECT
    )

    reranker = LLMRerank(
        choice_batch_size=retrieve_N_chunks,
        top_n=reranker_top_n,
        service_context=service_context,
        choice_select_prompt=choice_select_prompt
    )
    reranked_nodes = reranker.postprocess_nodes(
        nodes, query_bundle
    )

    print(f'\n\n{"=" * 20}\nRetrieved nodes\n\n')
    for node in nodes:
        print_node(node)

    print(f'\n\n{"=" * 20}\nReranked nodes\n\n')
    for node in reranked_nodes:
        print_node(node)

    return query_engine.synthesize(query_bundle=query_bundle, nodes=reranked_nodes), llama_debug


def print_debug(response: RESPONSE_TYPE, llama_debug: LlamaDebugHandler):
    event_pairs = llama_debug.get_event_pairs(CBEventType.LLM)
    print("\n" + ("=" * 20) + " RESPONSE " + ("=" * 20) + "\n")
    for node in response.source_nodes:
        print_node(node)
    print("\n" + ("=" * 20) + " /RESPONSE " + ("=" * 20) + "\n")
    print("\n" + ("=" * 20) + " DEBUG " + ("=" * 20) + "\n")
    for event_pair in event_pairs:
        print(event_pair[0])
        print(event_pair[1].payload.keys())
        print(event_pair[1].payload["response"])
    print("\n" + ("=" * 20) + " /DEBUG " + ("=" * 20) + "\n")


def print_node(node):
    print(f'{node.node_id}: score {node.score} - {node.node.metadata["file_name"]}\n\n')


response, llama_debug = query("Who is Captain Nemo")
print_debug(response, llama_debug)
