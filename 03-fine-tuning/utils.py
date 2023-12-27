from datasets import load_dataset
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import torch
from const import model_name, fine_tuned_folder, dataset_name, device_name, samples


def load_tokenized_datasets():
    def tokenize_function(examples):
        return tokenizer(examples["text"], padding="max_length", truncation=True)

    # load a dataset from HF
    dataset = load_dataset(dataset_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenized_datasets = dataset.map(tokenize_function, batched=True)

    # Remove the text column because the model does not accept raw text as an input:
    tokenized_datasets = tokenized_datasets.remove_columns(["text"])

    # Rename the label column to labels because the model expects the argument to be named labels:
    tokenized_datasets = tokenized_datasets.rename_column("label", "labels")

    # Set the format of the dataset to return PyTorch tensors instead of lists:
    tokenized_datasets.set_format("torch")

    return tokenized_datasets;

def load_model_and_device_from_hf():
    return load_model_and_device(model_name_or_path=model_name)

def load_fine_tuned_model_and_device():
    return load_model_and_device(model_name_or_path=f'{fine_tuned_folder}/{model_name}/{dataset_name}/{samples}')

def load_model_and_device(model_name_or_path):
    model = AutoModelForSequenceClassification.from_pretrained(model_name_or_path,
                                                               num_labels=5)
    device = torch.device(device_name)
    model.to(device)

    return model, device
