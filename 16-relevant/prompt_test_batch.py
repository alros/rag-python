from json import JSONDecodeError

import chromadb
from llama_index.legacy.callbacks import CallbackManager
from llama_index.legacy.llms import Ollama
from llama_index.legacy.query_engine import RetrieverQueryEngine
from llama_index.legacy.response_synthesizers import ResponseMode
from utils import *
import json

llm = Ollama(model=model)
collection = collection_dementia

llama_debug = LlamaDebugHandler(print_trace_on_end=True)
callback_manager = CallbackManager([llama_debug])
service_context = ServiceContext.from_defaults(llm=llm,
                                               embed_model="local",
                                               callback_manager=callback_manager)
db = chromadb.PersistentClient(path=db_path)

# Diagnosis prompt
system_prompt_diagnosis = """\
You are a medical system that can provide evaluations with associated confidence scores.
You only respond with valid JSON objects.
"""
user_prompt_diagnosis = """\
Context information is below.
<context>
{context_str}
</context>
Given the context information and not prior knowledge, answer the query.
Query: {query_str} How many symptoms of the disease does the patient have and how severe is the condition?
You will respond only with a JSON object with the key Number with the number of symptoms, the key Severity with the level of severity from 0 to 1, the key Confidence with the confidence from 0 to 1, and the key Explanation with the explanation.
Answer:
"""

tests = [
    {
        'd': 'The patient is a 75-year-old individual.',
        'e': 0,
        's': 0
    }, {
        'd': 'The patient is a 75-year-old individual occasionally experiencing difficulty remembering recent events.',
        'e': 0.1,
        's': 1
    }, {
        'd': 'The patient is a 75-year-old individual frequently experiencing difficulty remembering recent events.',
        'e': 0.2,
        's': 1
    }, {
        'd': 'The patient is a 75-year-old individual constantly experiencing difficulty remembering recent events.',
        'e': 0.3,
        's': 1
    }, {
        'd': 'The patient is a 75-year-old individual occasionally experiencing difficulty remembering recent events, and mild confusion.',
        'e': 0.2,
        's': 2
    }, {
        'd': 'The patient is a 75-year-old individual frequently experiencing difficulty remembering recent events, noticeable confusion.',
        'e': 0.4,
        's': 2
    }, {
        'd': 'The patient is a 75-year-old individual constantly experiencing difficulty remembering recent events, severe confusion.',
        'e': 0.6,
        's': 2
    }, {
        'd': 'The patient is a 75-year-old individual occasionally experiencing difficulty remembering recent events, mild confusion, occational episodes of disorientation.',
        'e': 0.3,
        's': 3
    }, {
        'd': 'The patient is a 75-year-old individual frequently experiencing difficulty remembering recent events, noticeable confusion, frequent episodes of disorientation.',
        'e': 0.6,
        's': 3
    }, {
        'd': 'The patient is a 75-year-old individual constantly experiencing difficulty remembering recent events, severe confusion, constant disorientation',
        'e': 0.9,
        's': 3
    }, {
        'd': 'The patient is a 16-year-old individual, constantly experiencing difficulty remembering recent events.',
        'e': 0,
        's': 0
    }, {
        'd': 'The patient is a 16-year-old individual, constantly experiencing difficulty remembering recent events.',
        'e': 0,  # adjusted by age
        's': 1
    }, {
        'd': 'The patient is a 55-year-old individual, constantly experiencing difficulty remembering recent events.',
        'e': 0.3,
        's': 1
    }, {
        'd': 'The patient is a 16-year-old individual, with poor concentration.',
        'e': 0,  # adjusted by age
        's': 1
    }, {
        'd': 'The patient is a 45-year-old individual, with severe lack of inibition, and frequent bingeing on sweet food.',
        'e': 0.6,
        's': 1
    }, {
        'd': 'The patient is a 65-year-old individual, with moderate memory problems, moderate problems reading and writing, and occasional sudden changes in mood.',
        'e': 0.6,
        's': 3
    }, {
        'd': 'The patient is a 65-year-old individual, with frequent tendency to fall, frequent episodes of confusions, and moderate tremors.',
        'e': 0.6,
        's': 3
    }, {
        'd': 'The patient is a 65-year-old individual, with a broken leg.',
        'e': 0,
        's': 0
    }, {
        'd': 'The patient is a 95-year-old individual, with a normal blood pressure, and a passion for chess.',
        'e': 0,
        's': 0
    }

]

max = 3

vector_retriever_chunk = get_vector_retriever_chunk(collection=collection,
                                                    db=db,
                                                    service_context=service_context)

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

results = []

for test in tests:
    description = test['d']
    expected_confidence = test['e']
    symptoms = test['s']
    response_diagnosis = query_engine_diagnosis.query(description)
    try:
        data = json.loads(response_diagnosis.response)
    except JSONDecodeError:
        data = {
            'Number': -1,
            'Synthetic': -1,
            'Confidence': -1
        }
    try:
        results.append({
            'Symptoms': symptoms,
            'Expected Confidence': expected_confidence,
            'Detected symptoms': data['Number'],
            'Severity': data['Severity'],
            'Confidence': data['Confidence']
        })
    except KeyError:
        print(f'ERROR: {data}')

max_diagnosis = 0
for result in results:
    result['Diagnosis'] = result["Detected symptoms"] * result['Severity']
    if result['Detected symptoms'] <= max:
        max_diagnosis = max_diagnosis if max_diagnosis > result['Diagnosis'] else result['Diagnosis']

for result in results:
    result['Diagnosis'] = result['Diagnosis'] / max_diagnosis if result['Detected symptoms'] <= max else 'N/A'

print('|Number of symptoms|Expected Confidence|Detected symptoms|Severity|Diagnosis|Confidence|Evaluation|')
print('|------------------|-------------------|-----------------|--------|---------|----------|----------|')
for result in results:
    evaluation = 1 - abs(result['Diagnosis'] - result["Expected Confidence"]) if result['Diagnosis'] != 'N/A' else 'N/A'
    print(f'|\
{result["Symptoms"]}|\
{result["Expected Confidence"]}|\
{result["Detected symptoms"]}|\
{result["Severity"]}|\
{result["Diagnosis"]}|\
{result["Confidence"]}|\
{evaluation}|')
