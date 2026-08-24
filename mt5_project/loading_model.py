import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google-t5/t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
