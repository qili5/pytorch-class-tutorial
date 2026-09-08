from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

result = classifier("PyTorch is fun to learn!")
print(result)  

result = classifier("This assignment is way too hard.")
print(result) 

sentences = "This assignment is way too hard"

tokenizer_dir = tokenizer(sentences, return_tensors="pt")
print(tokenizer_dir)

tokens = tokenizer.tokenize(sentences)
print(tokens)

ids = tokenizer.convert_tokens_to_ids(tokens)
print(ids)

decode_ids = tokenizer.convert_ids_to_tokens(ids)
print(decode_ids)

