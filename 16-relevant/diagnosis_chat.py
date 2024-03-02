import re

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

# Chat generation
system_prompt_chat_generation = """\
You are a Doctor.
Your patient may experience symptoms of dementia.
You are collecting information from a patient.
You always use a professional tone.
You never assume that Patient experiences symptoms. 
You always ask if Patient experiences a symptom.
You never repeat questions.
You talk directly to the patient."""
user_prompt_chat_generation = """\
This is the description of dementia:
---------------------
{context_str}
---------------------
This is the conversation with patient:
---------------------
{query_str}
---------------------
Generate your next question."""

# Summary generation
system_prompt_summary = """\
You are excellent at understanding the Patient's profile based on dialogs with you"""
user_prompt_summary = """\
This is the conversation with your patient:
---------------------
{query_str}
---------------------
Please define your patient in a sentence.
Answer:"""

# Diagnosis prompt
system_prompt_diagnosis = """\
<s>[INST]You are a Doctor.
You can provide medical advice.
Follow the instructions.[/INST]</s>"""
user_prompt_diagnosis = """\
<s>[INST]What is the probability that the patient is affect by the disease in the description.
Disease description:
---------------------
{context_str}
---------------------
Patient description:
---------------------
{query_str}
---------------------
Just generate the percentage of confidence without explanations.[/INST]</s>"""

# Questions
basic_questions = [
    'How old are you?',
    'Do you have any complain?'
]

vector_retriever_chunk = get_vector_retriever_chunk(collection=collection,
                                                    db=db,
                                                    service_context=service_context)

# Chat generation
text_template_chat_generation = get_prompt_template(system_prompt=system_prompt_chat_generation,
                                                    user_prompt=user_prompt_chat_generation)
query_engine_chat_generation = RetrieverQueryEngine.from_args(
    vector_retriever_chunk,
    service_context=service_context,
    verbose=True,
    response_mode=ResponseMode.COMPACT,
    text_qa_template=text_template_chat_generation
)

# Summary generation
text_template_summary = get_prompt_template(system_prompt=system_prompt_summary,
                                            user_prompt=user_prompt_summary)
query_engine_summary = RetrieverQueryEngine.from_args(
    NullRetriever(),
    service_context=service_context,
    verbose=True,
    response_mode=ResponseMode.COMPACT,
    text_qa_template=text_template_summary
)

# Diagnosis
text_template_diagnosis = get_prompt_template(system_prompt=system_prompt_diagnosis,
                                              user_prompt=user_prompt_diagnosis)
query_engine_diagnosis = RetrieverQueryEngine.from_args(
    vector_retriever_chunk,
    service_context=service_context,
    verbose=True,
    response_mode=ResponseMode.COMPACT,
    text_qa_template=text_template_diagnosis
)

questions_answers = []

enough = False
next_question = None
index_basic_questions = 0

while not enough:

    # Ask the next question

    if next_question is None and len(basic_questions) > index_basic_questions:
        next_question = basic_questions[index_basic_questions]
        index_basic_questions += 1
    elif len(basic_questions) == index_basic_questions:
        print('This is enough for today, I do not see any reason to worry')
        enough = True
        continue

    print(next_question)
    answer = input("Type your answer: ")

    questions_answers.append({
        'q': next_question,
        'a': answer
    })

    # Summarise the dialog

    query = '\n'.join([f'You: "{qa["q"]}"\nPatient: "{qa["a"]}"' for qa in questions_answers])

    response_summary = query_engine_summary.query(query)
    print("*" * 20)
    print("SUMMARY")
    print("*" * 20)
    print_debug(response=response_summary, llama_debug=llama_debug)

    # Try the diagnosis

    print("*" * 20)
    print("DIAGNOSIS")
    print("*" * 20)
    response_diagnosis = query_engine_diagnosis.query(response_summary.response)
    print_debug(response=response_diagnosis, llama_debug=llama_debug)

    if enough:
        #
        # TODO: This code is unreachable. Evaluate response_diagnosis
        #
        print('The final diagnosis is...')
        enough = True
        continue

    # Generate the next question

    query = '\n'.join([f'You: "{qa["q"]}"\nPatient: "{qa["a"]}"' for qa in questions_answers])
    response = query_engine_chat_generation.query(query)

    print_debug(response=response, llama_debug=llama_debug)

    next_question = response.response

    def extract_or_same(pattern:str, text:str, group:int):
        res = re.search('"(.*)"', next_question)
        return res.group(1) if not None else text

    next_question_clean = extract_or_same('"(.*)"', next_question, 1)

    # tmp = next_question.split("\n")
    # next_question_clean = tmp[len(tmp) - 1]
    # next_question_clean = next_question_clean.replace('You: ', '')
    # next_question_clean = re.search('"?([^"]*)"?', next_question_clean).group(2)
    print(f'DEBUG:\n{next_question}\n{next_question_clean}\n\n')
    next_question = next_question_clean
