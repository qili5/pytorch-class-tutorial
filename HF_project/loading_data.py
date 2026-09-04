from datasets import load_dataset
import pprint
# Download entire data
ds = load_dataset("openai/gsm8k",'main')
print(ds) # Basic info

train = ds["train"] # get the train split

pprint.pp(train.features) # Column names and types
pprint.pp(train[0])                        # first row as dict

print()
# Load just one split
# train = load_dataset("openai/gsm8k",'main', split="train")


# Stream huge datasets without downloading (lazy iteration)
ds = load_dataset("stanfordnlp/imdb", split="train", streaming=True)
# this dataset is much bigger
for example in ds.take(3):
    pprint.pp(example["text"])
# grab the first 3 examples from the dataset, and for each one, print just the question field.
