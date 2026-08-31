from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

result = generator(
    "I love python because",
    max_length=30,
    num_return_sequences=2,
)
print(result)
