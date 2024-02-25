from chromadb import ClientAPI
from langchain_core.retrievers import BaseRetriever
from llama_index import VectorStoreIndex, ChatPromptTemplate, ServiceContext
from llama_index.callbacks import CBEventType, LlamaDebugHandler
from llama_index.core.llms.types import MessageRole, ChatMessage
from llama_index.vector_stores import ChromaVectorStore

retrieve_N_chunks = 1

model = 'mistral'
context_window = 4096
chunk_size = context_window / 4

# Paths
db_path = './chroma_db/diagnosis'
kb_path = './symptoms'
db_collection = 'symptoms'


def print_debug(llama_debug: LlamaDebugHandler, response):
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


def get_vector_retriever_chunk(collection: str, db: ClientAPI, service_context: ServiceContext) -> BaseRetriever:
    chroma_collection = db.get_or_create_collection(collection)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    vector_store_index = VectorStoreIndex.from_vector_store(vector_store, service_context=service_context)
    return vector_store_index.as_retriever(similarity_top_k=retrieve_N_chunks)


def get_prompt_template(system_prompt: str, user_prompt: str):
    chat_text_qa_msgs = [
        ChatMessage(
            role=MessageRole.SYSTEM,
            content=system_prompt,
        ),
        ChatMessage(
            role=MessageRole.USER,
            content=user_prompt,
        ),
    ]
    return ChatPromptTemplate(chat_text_qa_msgs)
