from llama_index.legacy import SimpleDirectoryReader, StorageContext, VectorStoreIndex, load_index_from_storage, \
    ServiceContext, QueryBundle
import faiss
from llama_index.legacy.llms import Ollama
from llama_index.legacy.vector_stores import FaissVectorStore

dataset = '../datasets/gutenberg'
index_folder = './storage'
model = 'mistral'
question = 'Who is Captain Nemo?'
# derived from venvs/llm-python-310/lib/python3.10/site-packages/faiss/class_wrappers.py
# assert d == self.d
d = 384

llm = Ollama(model=model)
faiss_index = faiss.IndexFlatL2(d)
vector_store = FaissVectorStore(faiss_index=faiss_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
service_context = ServiceContext.from_defaults(llm=llm,
                                               embed_model="local")


def use_indexes():
    documents = SimpleDirectoryReader(dataset).load_data()

    index = VectorStoreIndex.from_documents(documents,
                                            service_context=service_context,
                                            storage_context=storage_context)
    index.storage_context.persist()

def _get_index_from_storage():
    vector_store = FaissVectorStore.from_persist_dir(index_folder)
    storage_context = StorageContext.from_defaults(vector_store=vector_store,
                                                   persist_dir=index_folder)
    return load_index_from_storage(storage_context=storage_context,
                                    service_context=service_context)

def query():
    index = _get_index_from_storage()
    query_engine = index.as_query_engine()
    response = query_engine.query(question)

    print(response)

    print('=' * 20 + '\n')
    for node in response.source_nodes:
        print(f'id={node.node_id} {node.metadata["file_name"]}\n')
        print(f'{node.text}\n\n')


def retrieve_only():
    index = _get_index_from_storage()

    query_engine = index.as_query_engine(similarity_top_k=500)
    q = QueryBundle(question)
    nodes = query_engine.retrieve(q)

    for i, node in enumerate(nodes):
        print(f'{i} id={node.node_id} {node.metadata["file_name"]} {node.score}')

# create_indexes()

# query()

retrieve_only()