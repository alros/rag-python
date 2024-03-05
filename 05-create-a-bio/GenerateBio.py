import logging
import sys

from llama_index import SimpleDirectoryReader, ServiceContext, StorageContext
from llama_index import VectorStoreIndex
from llama_index.callbacks import LlamaDebugHandler, CallbackManager, CBEventType
from llama_index.llms import Ollama
from llama_index.vector_stores import ChromaVectorStore
import chromadb

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

documents = SimpleDirectoryReader("../datasets/bio", recursive=True).load_data()
#llm = Ollama(model="llama2")
llm = Ollama(model="mistral")

llama_debug = LlamaDebugHandler(print_trace_on_end=True)
callback_manager = CallbackManager([llama_debug])

service_context = ServiceContext.from_defaults(llm=llm,
                                               embed_model="local",
                                               callback_manager=callback_manager)

db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("bio")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(documents,service_context=service_context,storage_context=storage_context)

query_engine = index.as_query_engine()
#response = query_engine.query("Generate the bio of a 95 years old woman born in Rome. Use at least 200 words.")
#response = query_engine.query("Who is Lucrezia?")
#response = query_engine.query("Generate a list of the Etruscan artifacts discovered by Lucrezia. For each artifact give me a description and where it is exposed today.")
#response = query_engine.query("Generate a list of the Roman mosaics discovered by Lucrezia. For each artifact give me a description and where it is exposed today.")
#response = query_engine.query("Generate examples of Lucrezia's dedication to preserving heritage.")
#response = query_engine.query("Generate a description of Lucretia's home in Trastevere.")
#response = query_engine.query("Generate an episode of particular significance in Lucrezia's life.")
#response = query_engine.query("Generate a new episode of particular significance in Lucrezia's life.")
#response = query_engine.query("Generate a new episode of Lucrezia's life when she was 90 years old. Don't repeat yourself.")
#response = query_engine.query("When did Lucrezia receive a visit of young archaeology students?")
response = query_engine.query("Summarise Lucrezia's life in 50 words.")
print("\n" + ("="*20) + "\nResponse:\n")
print(response)

event_pairs = llama_debug.get_event_pairs(CBEventType.LLM)

print("\n" + ("="*20) + "\n")

for event_pair in event_pairs:
    print(event_pair[0])
    print(event_pair[1].payload.keys())
    print(event_pair[1].payload["response"])
