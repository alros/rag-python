from torch.utils.data import DataLoader
import torch
import evaluate
from utils import load_tokenized_datasets, load_fine_tuned_model_and_device, load_model_and_device_from_hf


tokenized_datasets = load_tokenized_datasets()

small_eval_dataset = tokenized_datasets["test"].shuffle(seed=42).select(range(1000))

eval_dataloader = DataLoader(small_eval_dataset, batch_size=8)

model, device = load_fine_tuned_model_and_device()
#model, device = load_model_and_device_from_hf()

metric = evaluate.load("accuracy")
model.eval()
for batch in eval_dataloader:
    batch = {k: v.to(device) for k, v in batch.items()}
    with torch.no_grad():
        outputs = model(**batch)

    logits = outputs.logits
    predictions = torch.argmax(logits, dim=-1)
    metric.add_batch(predictions=predictions, references=batch["labels"])

res = metric.compute()

print(res)