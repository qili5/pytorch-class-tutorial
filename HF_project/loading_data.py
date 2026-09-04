from datasets import load_dataset

# Load a famous NLP benchmark for QA task
# ds = load_dataset("rajpurkar/squad")
# print(ds)

# DatasetDict({
#     train: Dataset({features: ['id','title','context','question','answers'], num_rows: 87599})
#     validation: Dataset({features: [...], num_rows: 10570})
# })

# Load just one split
# train = load_dataset("rajpurkar/squad", split="train")


# Stream huge datasets without downloading (lazy iteration)
ds = load_dataset("rajpurkar/squad", split="train", streaming=True)
for example in ds.take(3):
    print(example["question"])