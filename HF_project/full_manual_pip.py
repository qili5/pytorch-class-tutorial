from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

model_name = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

X_train = ["PyTorch is fun to learn!","This assignment is way too hard"]

#using huggingFace pipeline
results = classifier(X_train)
print(results)

manual_tokenization = tokenizer(X_train, return_tensors="pt", 
                                padding=True, truncation=True, max_length=512).to(device)
print(manual_tokenization)

with torch.no_grad():
    outputs = model(**manual_tokenization)
    print(outputs)
    predictions = F.softmax(outputs.logits, dim=-1)
    print(predictions)
    predicted_labels = torch.argmax(predictions, dim=1)
    print(predicted_labels)