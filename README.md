# rag-python
ML/LLM experiments with Llama Index to develop a personal assistant for cognitive impaired patients

## Datasets

The datasets come from Wikipedia and focus on dementia. 

## Setup

### Python scripts

`Python 3.11` is unsupported by `Pytorch`. The application must run with `Python 3.10`.

Install dependencies
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

Install `ollama`

```shell
brew install ollama
mkdir -p ~/.ollama
# optional to store the models on an external drive
ln -s "/{PATH}/ollama" ~/.ollama/models
ollama serve
ollama pull mistral
ollama pull llama2
```

Run it

```shell
ollama serve
ollama run llama2
```

That should open an interactive shell to chat with Llama2

## Experiments

### 01-use-local-knowledge

Basic experiment using `llama-index` and `llama` to index and query a dataset.

### 02-chat-bot

Experiment using `ollama`/`llama2` + `streamlit`/`landchan`/`chromadb` to discuss a PDF with the LLM

### 03-fine-tuning

Experiment fine-tuning `bert` with a dataset of reviews

### 04-training-with-colab

Same as 03, but using Colab