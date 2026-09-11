from transformers import pipeline

classifier = pipeline("zero-shot-classification")
list_of_inputs=[
   "This is a pytorch course learning about transformers and huggingface.",
   "Google company is a multinational technology company.",
]

result = classifier(
   list_of_inputs,
    candidate_labels=["education", "politics", "business"],
)

print(result)
