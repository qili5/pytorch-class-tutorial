from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("PyTorch is fun to learn!")
print(result)  # [{'label': 'POSITIVE', 'score': 0.99...}]

result = classifier("This assignment is way too hard.")
print(result)  # [{'label': 'NEGATIVE', 'score': 0.99...}]

# pipeline() also works on a list of inputs at once
results = classifier([
    "I love this class.",
    "I am so confused right now.",
])
print(results)
