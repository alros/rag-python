import chromadb
from llama_index.callbacks import CallbackManager
from llama_index.llms import Ollama
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.response_synthesizers import ResponseMode
from utils import *
from NullRetriever import NullRetriever

llm = Ollama(model=model)
collection = collection_dementia

llama_debug = LlamaDebugHandler(print_trace_on_end=True)
callback_manager = CallbackManager([llama_debug])
service_context = ServiceContext.from_defaults(llm=llm,
                                               embed_model="local",
                                               callback_manager=callback_manager)
db = chromadb.PersistentClient(path=db_path)

vector_retriever_chunk = get_vector_retriever_chunk(collection=collection,
                                                    db=db,
                                                    service_context=service_context)
#vector_retriever_chunk = NullRetriever()

system_prompt = """\
You only respond with valid JSON objects."""

user_prompt_summary = """\
Context information is below.
<context>
{context_str}
</context>
This is the conversation with the patient:
<conversation>
{query_str}
</conversation>
Given the conversation with the patient, and not prior knowledge, generate a question to find out if the patient experiences any symptom in the context.
You will respond only with a JSON object with the key Question with question for the patient, the key Explanation with the explanation."""

text_qa_template = get_prompt_template(system_prompt=system_prompt, user_prompt=user_prompt_summary)

query_engine_summary = RetrieverQueryEngine.from_args(
    vector_retriever_chunk,
    service_context=service_context,
    verbose=True,
    response_mode=ResponseMode.COMPACT,
    text_qa_template=text_qa_template
)

questions = [
    {
        'q': 'How old are you?',
        'a': '75'
    }
]
# questions = [
#     {
#         'q': 'How old are you?',
#         'a': '75'
#     }, {
#         'q': 'I\'d like to ask if you have noticed any memory loss or difficulty in recalling recent events?',
#         'a': 'yes, sometimes I forget where I am'
#     }, {
#         'q': 'I see. Have you also experienced any difficulty in recognizing familiar faces or objects recently?',
#         'a': 'No, I have never problems recognising people'
#     }
# ]


query = '\n'.join([f'You: "{qa["q"]}"\nPatient: "{qa["a"]}"' for qa in questions])

next_questions=[]
for i in range(0,10):
    response = query_engine_summary.query(query)
    next_questions.append(response.response)
    print(response.response)

for next_question in next_questions:
    print(f'- {next_question}\n')