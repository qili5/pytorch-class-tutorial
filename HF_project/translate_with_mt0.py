import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

CHECKPOINT = "bigscience/mt0-small"  # or "bigscience/mt0-large" for a larger model

# Same PyTorch device pattern as any other model: use a GPU if one's available
if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")  # Apple Silicon GPU
else:
    device = torch.device("cpu")
print("Using device:", device)

print(f"Loading {CHECKPOINT} (this may take a moment the first time)...")
tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT)
model = AutoModelForSeq2SeqLM.from_pretrained(CHECKPOINT).to(device)
model.eval()  # inference mode

def translate(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_new_tokens=50
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

file_path = "translate_examples.txt"
with open(file_path, "r") as file:
    examples = file.read()
examples_file = examples.strip().splitlines()

for prompt in examples_file:
    print(f"\nPrompt: {prompt}")
    print(f"Output: {translate(prompt)}")

