from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("google-t5/t5-small")

text = "summarize: PyTorch is a popular deep learning framework."

inputs = tokenizer(text, return_tensors="pt")

print(inputs)

