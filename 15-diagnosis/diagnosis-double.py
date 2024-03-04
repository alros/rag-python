import chromadb
from llama_index.legacy import ServiceContext, VectorStoreIndex, ChatPromptTemplate
from llama_index.legacy.callbacks import LlamaDebugHandler, CallbackManager, CBEventType
from llama_index.legacy.core.llms.types import MessageRole, ChatMessage
from llama_index.legacy.llms import Ollama
from llama_index.legacy.query_engine import RetrieverQueryEngine
from llama_index.legacy.response_synthesizers import ResponseMode
from llama_index.legacy.vector_stores import ChromaVectorStore

model = 'mistral'
context_window = 4096
chunk_size = context_window / 4

# Paths
db_path = './chroma_db/diagnosis'
kb_path = './symptoms'
db_collection = 'symptoms'

# Retrieval
retrieve_N_chunks = 3

# Depression short
# questions_answers = [
#     {
#         'q': 'Do you feel persecuted by people around you?',
#         'a': 'Yes.'
#     }, {
#         'q': 'Do you run from people and barricade in your apartment?',
#         'a': 'Yes, sometimes I hide for days.'
#     }
# ]

# Depression medium
# questions_answers = [
#     {
#         'q': 'What do you do in your free time?',
#         'a': 'The usual, I watch tv.'
#     }, {
#         'q': 'Don\'t you want to do anything else?',
#         'a': 'No, I don\'t'
#     }, {
#         'q': 'How often do you see friends? ',
#         'a': 'I don\'t know, not very often'
#     }
# ]

# Depression long
questions_answers = [
    {
        'q': 'What do you do in your free time?',
        'a': 'The usual, I watch tv.'
    }, {
        'q': 'Don\'t you want to do anything else?',
        'a': 'No, I don\'t'
    }, {
        'q': 'How often do you see friends?',
        'a': 'I don\'t know, not very often.'
    }, {
        'q': 'Do you prefer to stay alone?',
        'a': 'Yes, I guess so. I always feel tired.'
    }, {
        'q': 'Do you sleep well at night?',
        'a': 'I wake up often, and I make bad dreams.'
    }, {
        'q': 'Do you ever have negative thoughts?',
        'a': 'Like suicide? Sometimes.'
    }
]

# Normal
# questions_answers = [
#     {
#         'q': 'What do you do in your free time?',
#         'a': 'The usual, I watch tv, I go out with friends.'
#     }, {
#         'q': 'Don\'t you want to do anything else?',
#         'a': 'Yes, I\'d love to do sport but I\'m too busy'
#     }, {
#         'q': 'How often do you see friends? ',
#         'a': 'I don\'t know, some once or twice a week, others once a month.'
#     }
# ]

# Normal alt
# questions_answers = [
#     {
#         'q': 'What do you do in your free time?',
#         'a': 'The usual, I watch tv, I go out with friends.'
#     }, {
#         'q': 'Don\'t you want to do anything else?',
#         'a': 'Yes, I\'d love to do more sport but I\'m too busy with my project!'
#     }, {
#         'q': 'How often do you see friends? ',
#         'a': 'Quite often, some once or twice a week, others once a month.'
#     }
# ]

llm = Ollama(model=model)

llama_debug = LlamaDebugHandler(print_trace_on_end=True)
callback_manager = CallbackManager([llama_debug])

service_context = ServiceContext.from_defaults(llm=llm,
                                               embed_model="local",
                                               callback_manager=callback_manager)

db = chromadb.PersistentClient(path=db_path)


def get_vector_retriever_chunk(collection: str):
    chroma_collection = db.get_or_create_collection(collection)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    vector_store_index = VectorStoreIndex.from_vector_store(vector_store, service_context=service_context)
    return vector_store_index.as_retriever(similarity_top_k=retrieve_N_chunks)


vector_retriever_chunk = get_vector_retriever_chunk('Depression')

# user_prompt="""\
# Context information is below.
# ---------------------
# {context_str}
# ---------------------
# Given the context information and not prior knowledge,
# Given the following chat:
# ---------------------
# {query_str}
# ---------------------
# Reply with the name of the three most probable disease and the degree of confidence.
# Example: disease1 50%, disease2 35%, disease3 15%
# Do not add extra information."""

# user_prompt="""\
# {query_str}
# The disease in exam can be described as:
# ---------------------
# {context_str}
# ---------------------
# The probability that the Patient is affected by the disease is:"""
user_prompt = """\
Context information is below.
---------------------
{context_str}
---------------------
{query_str}
Reply with yes or no.
Is this enough to determine if the patient is affected by the disease in the context?"""

user_prompt_summary = """\
This is the conversation with your patient:
---------------------
{query_str}
---------------------
Please define your patient in a sentence.
Answer:"""

system_prompt = """\
You are a Doctor.
You can provide medical advice."""

system_prompt_summary = """\
You are excellent at understanding the Patient's profile based on dialogs with you"""

chat_text_qa_msgs = [
    ChatMessage(
        role=MessageRole.SYSTEM,
        content=(system_prompt),
    ),
    ChatMessage(
        role=MessageRole.USER,
        content=(user_prompt),
    ),
]
chat_text_qa_msgs_summary = [
    ChatMessage(
        role=MessageRole.SYSTEM,
        content=(system_prompt_summary),
    ),
    ChatMessage(
        role=MessageRole.USER,
        content=(user_prompt_summary),
    ),
]

text_qa_template = ChatPromptTemplate(chat_text_qa_msgs_summary)

query_engine = RetrieverQueryEngine.from_args(
    vector_retriever_chunk,
    service_context=service_context,
    verbose=True,
    response_mode=ResponseMode.COMPACT,
    text_qa_template=text_qa_template
)

query = '\n'.join([f'You: "{qa["q"]}"\nPatient: "{qa["a"]}"' for qa in questions_answers])

response = query_engine.query(query)


def print_debug():
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


print_debug()

print("*" * 40)

text_qa_template = ChatPromptTemplate(chat_text_qa_msgs)

query_engine = RetrieverQueryEngine.from_args(
    vector_retriever_chunk,
    service_context=service_context,
    verbose=True,
    response_mode=ResponseMode.COMPACT,
    text_qa_template=text_qa_template
)
response = query_engine.query(response.response)

print_debug()
