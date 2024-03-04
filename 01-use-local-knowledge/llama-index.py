import os
import time
from llama_index.legacy import (
    VectorStoreIndex,
    ServiceContext,
    SimpleDirectoryReader,
    set_global_service_context,
    StorageContext,
    load_index_from_storage
)
from llama_index.legacy.llms import HuggingFaceLLM
from llama_index.legacy.prompts import PromptTemplate
import torch
from transformers import AutoModelForCausalLM

LLAMA2_7B = "meta-llama/Llama-2-7b-hf"
LLAMA2_7B_CHAT = "meta-llama/Llama-2-7b-chat-hf"
LLAMA2_13B = "meta-llama/Llama-2-13b-hf"
LLAMA2_13B_CHAT = "meta-llama/Llama-2-13b-chat-hf"
LLAMA2_70B = "meta-llama/Llama-2-70b-hf"
LLAMA2_70B_CHAT = "meta-llama/Llama-2-70b-chat-hf"
ORCA_7B = "microsoft/Orca-2-7b"

# Settings
prompt = 'Are dementia patients more likely to be visited by aliens?'
device = 'mps'
model_name = ORCA_7B
max_time = None
do_sample = True
embed_model = "local:BAAI/bge-small-en"
#data_folder = "dementia-wiki-txt"
data_folder = "dementia-wiki-polluted"
root_data_folder = "../datasets"
index_storage_folder = f'../index-storage/{model_name}/{data_folder}'
context_window = 4096
max_new_tokens = 2048
generate_kwargs = {
    # do_sample: if set to True, this parameter enables decoding strategies such as multinomial sampling, beam-search
    # multinomial sampling, Top-K sampling and Top-p sampling. All these strategies select the next token from the
    # probability distribution over the entire vocabulary with various strategy-specific adjustments.
    "do_sample": do_sample,

    # max_new_tokens: the maximum number of tokens to generate. In other words, the size of the output sequence, not
    # including the tokens in the prompt. As an alternative to using the output’s length as a stopping criteria, you can
    # choose to stop generation whenever the full generation exceeds some amount of time.
    #"max_new_tokens": ???

    # num_beams: by specifying a number of beams higher than 1, you are effectively switching from greedy search to beam
    # search. This strategy evaluates several hypotheses at each time step and eventually chooses the hypothesis that
    # has the overall highest probability for the entire sequence. This has the advantage of identifying
    # high-probability sequences that start with a lower probability initial tokens and would’ve been ignored by the
    # greedy search.
    "num_beams": 1,

    # num_return_sequences: the number of sequence candidates to return for each input. This option is only available
    # for the decoding strategies that support multiple sequence candidates, e.g. variations of beam search and
    # sampling. Decoding strategies like greedy search and contrastive search return a single output sequence.
    "num_return_sequences": 1,

    # min_length: (Default: None). Integer to define the minimum length in tokens of the output summary.
    "min_length": None,

    # max_length: (Default: None). Integer to define the maximum length in tokens of the output summary.
    "max_length": None,

    # top_k: (Default: None). Integer to define the top tokens considered within the sample operation to create new
    # text.
    "top_k": None,

    # top_p: (Default: None). Float to define the tokens that are within the sample operation of text generation. Add
    # tokens in the sample for more probable to least probable until the sum of the probabilities is greater than top_p.
    "top_p": None,

    # temperature: (Default: 1.0). Float (0.0-100.0). The temperature of the sampling operation. 1 means regular
    # sampling, 0 means always take the highest score, 100.0 is getting closer to uniform probability.
    "temperature": 0.01,

    # repetition_penalty: (Default: None). Float (0.0-100.0). The more a token is used within generation the more it is
    # penalized to not be picked in successive generation passes.
    "repetition_penalty": None,

    #max_time: (Default: None). Float (0-120.0). The amount of time in seconds that the query should take maximum.
    # Network can cause some overhead so it will be a soft limit.
    "max_time": max_time,

}
torch_dtype = torch.float16
load_in_8bit = False
system_prompt = """You are an AI assistant that answers questions with  professional tone, based on the given source documents.
You must follow these rules:
- Generate human readable output.
- Do not generate gibberish text.
- Generate only the requested output
- Do not repeat the prompt in your output.
- Never generate offensive or foul language.
- The context always tells the truth and takes precedence over previous knowledge.
"""

# Code
query_wrapper_prompt = PromptTemplate(
    "[INST]<<SYS>>\n" + system_prompt + "<</SYS>>\n\n{query_str}[/INST] "
)

model = AutoModelForCausalLM.from_pretrained(model_name,
                                             num_labels=5,
                                             # token=token,
                                             torch_dtype=torch_dtype,
                                             device_map=device,
                                             load_in_8bit=load_in_8bit)

llm = HuggingFaceLLM(
    context_window=context_window,
    max_new_tokens=max_new_tokens,
    generate_kwargs=generate_kwargs,
    query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name=model_name,
    model=model)


def load_index(llm, index_storage_folder, data_folder):
    service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)
    if not os.path.exists(index_storage_folder):
        set_global_service_context(service_context)
        documents = SimpleDirectoryReader(data_folder).load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=index_storage_folder)
        return index
    storage_context = StorageContext.from_defaults(persist_dir=index_storage_folder)
    return load_index_from_storage(storage_context, service_context=service_context)


index = load_index(llm=llm,
                   index_storage_folder=index_storage_folder,
                   data_folder=f'{root_data_folder}/{data_folder}')

query_engine = index.as_query_engine()

start = time.time()
response = query_engine.query(prompt)
end = time.time()

print('\n\n========== response ==========\n')
print(f"\n{response.response}\n")
print(f'\n\ngenerated in {end - start} seconds')
