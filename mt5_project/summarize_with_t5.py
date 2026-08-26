import torch
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

CHECKPOINT = "google-t5/t5-large"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

print(f"Loading {CHECKPOINT} (this may take a moment the first time)...")
tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT)
model = AutoModelForSeq2SeqLM.from_pretrained(CHECKPOINT).to(device)
model.eval()

def summarize(paragraph: str) -> str:
    # T5 needs a task prefix/prompt to know what to do with the input
    prompt = "summarize: " + paragraph

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_new_tokens=50
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

file_path = "mt5_project/sample_paragraph.txt"
with open(file_path, "r") as file:
    paragraph_path = file.read()
paragraph = paragraph_path.strip()

print("\nOriginal paragraph:\n", paragraph)
print("\nSummary:\n", summarize(paragraph))

