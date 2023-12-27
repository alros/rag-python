from torch.utils.data import DataLoader
from torch.optim import AdamW
from transformers import get_scheduler
from tqdm.auto import tqdm
from const import model_name, dataset_name, fine_tuned_folder, num_epochs, samples
from utils import load_tokenized_datasets, load_model_and_device_from_hf

tokenized_datasets = load_tokenized_datasets()

small_train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(samples))

train_dataloader = DataLoader(small_train_dataset, shuffle=True, batch_size=8)

model, device = load_model_and_device_from_hf()

optimizer = AdamW(model.parameters(), lr=5e-5)

num_training_steps = num_epochs * len(train_dataloader)
lr_scheduler = get_scheduler(name="linear",
                             optimizer=optimizer,
                             num_warmup_steps=0,
                             num_training_steps=num_training_steps)

progress_bar = tqdm(range(num_training_steps))

model.train()
for epoch in range(num_epochs):
    for batch in train_dataloader:
        batch = {k: v.to(device) for k, v in batch.items()}
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()

        optimizer.step()
        lr_scheduler.step()
        optimizer.zero_grad()
        progress_bar.update(1)

model.save_pretrained(f'{fine_tuned_folder}/{model_name}/{dataset_name}/{samples}')
