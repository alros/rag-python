import chromadb
from llama_index.callbacks import CallbackManager
from llama_index.llms import Ollama
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.response_synthesizers import ResponseMode

from NullRetriever import NullRetriever
from diagnosisFinalQuestions import *
from diagnosisFinalUtils import *

question = questions_answers_normal2

llm = Ollama(model=model)
llama_debug = LlamaDebugHandler(print_trace_on_end=True)
callback_manager = CallbackManager([llama_debug])
service_context = ServiceContext.from_defaults(llm=llm,
                                               embed_model="local",
                                               callback_manager=callback_manager)
db = chromadb.PersistentClient(path=db_path)

vector_retriever_chunk = get_vector_retriever_chunk(collection='Depression',
                                                    db=db,
                                                    service_context=service_context)
null_retriever = NullRetriever()

# user_prompt = """\
# Context information is below.
# ---------------------
# {context_str}
# ---------------------
# {query_str}
# Reply with yes or no.
# Is this enough to determine if the patient is affected by the disease in the context?"""
user_prompt = """\
Context information is below.
---------------------
{context_str}
---------------------
{query_str}
What is the probability that the Patient is affected by the disease in the context?
Percentage:"""

user_prompt_summary = """\
This is the conversation with your patient:
---------------------
{query_str}
---------------------
Please define your patient in a sentence.
Answer:"""

system_prompt = """\
You are a Doctor.
You reply with a percentage and do not add further explanations.
Example: 15%."""

system_prompt_summary = """\
You are excellent at understanding the Patient's profile based on dialogs with you"""

text_qa_template_summary = get_prompt_template(system_prompt=system_prompt_summary, user_prompt=user_prompt_summary)
text_qa_template = get_prompt_template(system_prompt=system_prompt, user_prompt=user_prompt)

query = '\n'.join([f'You: "{qa["q"]}"\nPatient: "{qa["a"]}"' for qa in question])

query_engine_summary = RetrieverQueryEngine.from_args(
    NullRetriever(),
    service_context=service_context,
    verbose=True,
    response_mode=ResponseMode.COMPACT,
    text_qa_template=text_qa_template_summary
)

query_engine = RetrieverQueryEngine.from_args(
    vector_retriever_chunk,
    service_context=service_context,
    verbose=True,
    response_mode=ResponseMode.COMPACT,
    text_qa_template=text_qa_template
)

response = query_engine_summary.query(query)

print_debug(response=response, llama_debug=llama_debug)
print("*" * 40)

response = query_engine.query(response.response)

print_debug(response=response, llama_debug=llama_debug)
print("*" * 40)

print(("=" * 20) + 'FINAL RESPONSE' + ("=" * 20))
print(response.response)
