import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# pipeline() is convenient, but it's hiding 3 steps -- and it's hiding that
# this is ALL just PyTorch underneath. Here it is manually, using the same
# torch concepts from earlier: device, tensors, no_grad.
checkpoint = "bigscience/mt0-small"

# Step 1: load the tokenizer that matches the model
# (converts text <-> the numeric IDs the model actually understands)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

# Step 2: load the pretrained model -- this is a real torch.nn.Module
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
print("Is this a PyTorch model?", isinstance(model, torch.nn.Module))

# Step 3: pick a device, same pattern as any other PyTorch model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)          # move the model's weights onto that device
model.eval()                      # inference mode (turns off dropout, etc.)
print("Using device:", device)

# Step 4: tokenize text into PyTorch tensors, then move them to the same device
prompt = "Translate to English: Je t'aime."
inputs = tokenizer(prompt, return_tensors="pt")  # "pt" = PyTorch tensors
inputs = {k: v.to(device) for k, v in inputs.items()}

# These are ordinary tensors -- same .shape / .dtype you've already seen
print("input_ids:", inputs["input_ids"])
print("input_ids shape:", inputs["input_ids"].shape)
print("input_ids dtype:", inputs["input_ids"].dtype)

# Step 5: run the model. torch.no_grad() turns off gradient tracking --
# we're not training, just doing a forward pass, so this saves memory/compute.
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=50)
print("Raw output tokens:", outputs)

# Step 6: decode the output tokens back into text
text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Decoded output:", text)
