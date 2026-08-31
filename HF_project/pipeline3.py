from transformers import pipeline

classifier = pipeline("zero-shot-classification")

result = classifier(
    "This is a course about Python list comprehension",
    candidate_labels=["education", "politics", "business"],
)

print(result)
