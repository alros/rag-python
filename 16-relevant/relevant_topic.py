import re

import chromadb
from llama_index.legacy.callbacks import CallbackManager
from llama_index.legacy.llms import Ollama
from llama_index.legacy.query_engine import RetrieverQueryEngine
from llama_index.legacy.response_synthesizers import ResponseMode
from utils import *

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

system_prompt = """\
You are a Doctor.
Your patient may experience symptoms of dementia.
You are collecting information from a patient.
You always use a professional tone.
You never assume that Patient experiences symptoms. 
You always ask if Patient experiences a symptom.
You never repeat questions.
You talk directly to the patient."""

user_prompt_summary = """\
This is the description of dementia:
---------------------
{context_str}
---------------------
This is the conversation with patient:
---------------------
{query_str}
---------------------
Generate your next question."""

text_qa_template = get_prompt_template(system_prompt=system_prompt, user_prompt=user_prompt_summary)

query_engine_summary = RetrieverQueryEngine.from_args(
    vector_retriever_chunk,
    service_context=service_context,
    verbose=True,
    response_mode=ResponseMode.COMPACT,
    text_qa_template=text_qa_template
)

basic_questions = [
    'How old are you?',
    'Do you have any complain?'
]

questions = []

enough = False
next_question = None
index_basic_questions = 0
while not enough:
    if next_question is None and len(basic_questions) > index_basic_questions:
        next_question = basic_questions[index_basic_questions]
        index_basic_questions += 1
    elif len(basic_questions) == index_basic_questions:
        print('This is enough for today, I do not see any reason to worry')
        enough = True

    print(next_question)
    answer = input("Type your answer: ")

    questions.append({
        'q': next_question,
        'a': answer
    })

    query = '\n'.join([f'You: "{qa["q"]}"\nPatient: "{qa["a"]}"' for qa in questions])
    response = query_engine_summary.query(query)

    print_debug(response=response, llama_debug=llama_debug)

    next_question = response.response

    tmp = next_question.split("\n")
    next_question_clean = tmp[len(tmp)-1]
    next_question_clean = next_question_clean.replace('You: ', '')
    next_question_clean = re.search('"?([^"]*)"?', next_question_clean).group(1)
    print(f'DEBUG:\n{next_question}\n{next_question_clean}\n\n')
    next_question = next_question_clean
