import re

import chromadb
from llama_index.legacy.callbacks import CallbackManager
from llama_index.legacy.llms import Ollama
from llama_index.legacy.query_engine import RetrieverQueryEngine
from llama_index.legacy.response_synthesizers import ResponseMode
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

# Diagnosis prompt
system_prompt_diagnosis = """\
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide one short diagnosis, along with their confidence scores, and a synthetic number."""
user_prompt_diagnosis = """\
Context information is below.
<context>
{context_str}
</context>
Given the context information and not prior knowledge, answer the query.
Query: {query_str} How many symptoms of the disease does the patient have?
You will only respond with a JSON object with the key Synthetic with the requested number, Summary with the explanation and Confidence. Do not provide explanations.
Answer:
"""

#description = 'The patient is a 75-year-old individual.'
description = 'The patient is a 75-year-old individual experiencing mild memory lapses and forgetfulness, as reported by their spouse.'
#description = 'The patient is a 75-year-old individual experiencing memory lapses and cognitive impairment, as evidenced by forgetting to take medications, misplacing familiar routes, and difficulty recalling names.'
#description = 'The patient is a 75-year-old individual who experiences forgetfulness, confusion, and disorientation, as evidenced by frequent episodes of misplacing items, forgetting to take medications, difficulty remembering names and directions, and getting lost in familiar places.'


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

response_diagnosis = query_engine_diagnosis.query(description)
print_debug(response=response_diagnosis, llama_debug=llama_debug)
