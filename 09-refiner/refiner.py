import chromadb
from llama_index import ServiceContext, VectorStoreIndex
from llama_index.callbacks import LlamaDebugHandler, CallbackManager, CBEventType
from llama_index.llms import Ollama
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.response.schema import RESPONSE_TYPE
from llama_index.response_synthesizers import ResponseMode
from llama_index.vector_stores import ChromaVectorStore

model = "mistral"
db_path = '../chroma_db/gutenberg'
kb_path = './kb'
db_collection = 'gutenberg'
retrieve_N_chunks = 3


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

    return query_engine.query(prompt), llama_debug


def print_debug(response: RESPONSE_TYPE, llama_debug: LlamaDebugHandler):
    event_pairs = llama_debug.get_event_pairs(CBEventType.LLM)
    print("\n" + ("=" * 20) + " RESPONSE " + ("=" * 20) + "\n")
    for node in response.source_nodes:
        print(f'{node.node_id}: score {node.score} - {node.node.metadata["file_name"]}\n\n')
    print("\n" + ("=" * 20) + " /RESPONSE " + ("=" * 20) + "\n")
    print("\n" + ("=" * 20) + " DEBUG " + ("=" * 20) + "\n")
    for event_pair in event_pairs:
        print(event_pair[0])
        print(event_pair[1].payload.keys())
        print(event_pair[1].payload["response"])
    print("\n" + ("=" * 20) + " /DEBUG " + ("=" * 20) + "\n")


response, llama_debug = query("Who is Captain Name")
print_debug(response, llama_debug)
