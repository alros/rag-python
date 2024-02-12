# rag-python
ML/LLM experiments with Llama Index to develop a personal assistant for cognitive impaired patients.

## Index

- [Setup](#setup)
  - [Python scripts](#python-scripts)
  - [Ollama](#ollama)
- [Experiments](#experiments)
- [Datasets](#datasets)

Alternative indexing techniques using the FAISS library.

## Setup

### Python scripts

`Python 3.11` is unsupported by `Pytorch`. The application must run with `Python 3.10`.

Install dependencies:
```shell
pip install -r requirements.txt
# additional dependencies
pip install pypdf fastembed chromadb accelerate streamlit langchainhub
```

In some scripts, the value `device` must reflect the hardware:
- `auto` is the default 
- `cpu` should always work, but processing time will be too long
- `mps` to use M1

Some scripts connect to HuggingFace. Set the following environment variables:
- `HF_HOME=path`: path of the HuggingFace cache
- `HUGGING_FACE_HUB_TOKEN=token`: HuggingFace token to download the models

### Ollama

Ollama is required for most scripts.

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

- [01-use-local-knowledge](01-use-local-knowledge/README.md): basic experiment using `llama-index` and `llama` to index and query a dataset.
- [02-chat-bot](02-chat-bot/README.md): experiment using `ollama`/`llama2` + `streamlit`/`landchan`/`chromadb` to discuss a PDF with the LLM.
- [03-fine-tuning](03-fine-tuning/README.md): experiment fine-tuning `bert` with a dataset of reviews.
- [04-training-with-colab](04-training-with-colab/README.md): same as 03, but using Colab.
- [05-create-a-bio](05-create-a-bio/README.md): generate knowledge with LLMs and use the results to build the knowledge base for further iterations.
- [06-sentence-split](06-sentence-split/README.md): evaluates how SentenceSplitter works.
- 07-rag-pipeline: variation of 06-sentence-split.
- [08-query-chroma](08-query-chroma/README.md): test to verify how Chroma retrieves knowledge based on queries and filters.
- [09-refiner](09-refiner/README.md): utilisation of LLMs to re-rank results from the vector database.
- [10-keywords-extraction](10-keywords-extraction/README.md): methods to extract keywords (or key-phrases) from a text.
- [11-query-chroma-with-kw](11-query-chroma-with-kw/README.md): use keywords to pre-filter the nodes returned by a query.
- [12-faiss](12-faiss/README.md): alternative indexing techniques using the FAISS library.

## Datasets

- bio: the bio of a fictional woman generated by an [05-create-a-bio](05-create-a-bio/README.md).
- bio-single-file: like _bio_ but in a single file.
- dementia-wiki-txt: an extract of the [Wikipedia page about dementia](https://en.wikipedia.org/wiki/Dementia).
- dementia-wiki-polluted: same as _dementia-wiki-txt_ but polluted by a sentence affirming that there exists a relation between dementia and alien kidnapping (to study hallucinations).
- TwentyThousandLeaguesUnderTheSea: _Twenty Thousand Leagues Under the Seas_ by Jules Verne. Source: [https://www.gutenberg.org/](https://www.gutenberg.org/)
- gutenberg: five books from [https://www.gutenberg.org/](https://www.gutenberg.org/). _On the Origin of Species By Means of Natural Selection_ by Charles Darwin, _Paradise Lost_ by John Milton, _The Fall of the House of Usher_ by Edgar Allan Poe, _The Republic_ by Plato, and _Twenty Thousand Leagues under the Sea_ by Jules Verne.
