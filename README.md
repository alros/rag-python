# rag-python
ML/LLM experiments with Llama Index to develop a personal assistant for cognitive impaired patients

## Datasets

The datasets come from Wikipedia and focus on dementia. 

## Setup

Install dependencies
```sh
pip install -r requirements.txt
```

The value `device` must reflect the hardware:
- `auto` is the default 
- `cpu` should always work, but processing time will be too long
- `mps` to use M1

Set the following environment variables:
- `HF_HOME=path`: path of the HuggingFace cache
- `HUGGING_FACE_HUB_TOKEN=token`: HuggingFace token to download the models

## Experiments

### 01-use-local-knowledge

Basic experiment using `llama-index` and `llama` to index and query a dataset.