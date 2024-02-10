# rag-python
ML/LLM experiments with Llama Index to develop a personal assistant for cognitive impaired patients.

## Datasets

The datasets come from Wikipedia and focus on dementia. 

## Setup

### Python scripts

`Python 3.11` is unsupported by `Pytorch`. The application must run with `Python 3.10`.

Install dependencies:
```shell
pip install -r requirements.txt
# additional dependencies
pip install pypdf fastembed chromadb accelerate streamlit langchainhub
```

The value `device` must reflect the hardware:
- `auto` is the default 
- `cpu` should always work, but processing time will be too long
- `mps` to use M1

Set the following environment variables:
- `HF_HOME=path`: path of the HuggingFace cache
- `HUGGING_FACE_HUB_TOKEN=token`: HuggingFace token to download the models

### Ollama

Install `ollama`:

```shell
brew install ollama
mkdir -p ~/.ollama
# optional to store the models on an external drive
ln -s "/{PATH}/ollama" ~/.ollama/models
ollama serve
ollama pull mistral
ollama pull llama2
```

Run it:

```shell
ollama serve
ollama run llama2
```

That should open an interactive shell to chat with Llama2.

## Experiments

### 01-use-local-knowledge

Basic experiment using `llama-index` and `llama` to index and query a dataset.

### 02-chat-bot

Experiment using `ollama`/`llama2` + `streamlit`/`landchan`/`chromadb` to discuss a PDF with the LLM.

### 03-fine-tuning

Experiment fine-tuning `bert` with a dataset of reviews.

### 04-training-with-colab

Same as 03, but using Colab.

### 05-create-a-bio

Generate knowledge with LLMs and use the results to build the knowledge base for further iterations.

### 06-sentence-split

Evaluates how SentenceSplitter works.

### 07-rag-pipeline

Variation of 06-sentence-split.

### 08-query-chroma

Test to verify how Chroma retrieves knowledge based on queries and filters.

## 09-refiner

Utilisation of LLMs to re-rank results from the vector database.

## 10-keywords-extraction

Methods to extract keywords (or key-phrases) from a text.

## 11-query-chroma-with-kw

Use keywords to pre-filter the nodes returned by a query.

## Datasets

- `bio`: fictional bio generated iteratively with `05-create-a-bio`.
- `bio-single-file`: same as `bio` but in one file.
- `dementia-wiki-txt`: extract from the Wikipedia about dementia.
- `dementia-wiki-polluted`: same as `dementia-wiki-txt` but contains a sentence connecting dementia to alien abduction. It's useful to evaluate LLMs' hallucination in RAG.
- `TwentyThousandLeaguesUnderTheSea`: "Twenty Thousand Leagues Under The Sea" from [https://www.gutenberg.org/ebooks/164](https://www.gutenberg.org)
- `gutemberg`: a few free books from [https://www.gutenberg.org](https://www.gutenberg.org)
