from llama_index import ServiceContext, ChatPromptTemplate
from llama_index.callbacks import LlamaDebugHandler, CallbackManager
from llama_index.core.llms.types import ChatMessage, MessageRole
from llama_index.llms import Ollama
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.response_synthesizers import ResponseMode

from NullRetriever import NullRetriever

diagnosis = """
Based on the information provided in the context, a 75-year-old individual can experience various symptoms of dementia
such as memory loss, poor concentration, difficulty recognizing people or objects, confusion, disorientation, slow
speech, problems with everyday tasks, and decision-making. The most common types of dementia in older adults are
Alzheimer's disease and vascular dementia, both of which can present with these symptoms. Given the age of the
individual, it is likely that they may be experiencing multiple symptoms, making the total number of symptoms difficult
to quantify precisely. However, considering the information provided, we can estimate that the patient may be
experiencing around 10 symptoms. The severity level is set to 0.8 based on the context description, which suggests
significant impairment but not complete loss of cognitive function. The confidence score is high as the diagnosis is
based on well-established information about dementia and its common symptoms.
"""

llm = Ollama(model='mistral')

llama_debug = LlamaDebugHandler(print_trace_on_end=True)
callback_manager = CallbackManager([llama_debug])
service_context = ServiceContext.from_defaults(llm=llm,
                                               embed_model="local",
                                               callback_manager=callback_manager)
vector_retriever_chunk = NullRetriever()

system_prompt = """\
You are a doctor talking with your patient.
You speak clearly, with a professional tone."""

user_prompt = """\
Context information is below.
<context>
{context_str}
</context>
Given this diagnosis of the patient:
<diagnosis>
{query_str}
</diagnosis>
Explain the diagnosis to the patient talking directly to him."""

text_qa_template = ChatPromptTemplate([
    ChatMessage(
        role=MessageRole.SYSTEM,
        content=system_prompt,
    ),
    ChatMessage(
        role=MessageRole.USER,
        content=user_prompt,
    ),
])

query_engine = RetrieverQueryEngine.from_args(
    vector_retriever_chunk,
    service_context=service_context,
    verbose=True,
    response_mode=ResponseMode.COMPACT,
    text_qa_template=text_qa_template
)

print(query_engine.query(diagnosis))
