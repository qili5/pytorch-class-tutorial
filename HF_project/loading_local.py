from datasets import load_dataset, Dataset
import pandas as pd

# From CSV
# ds = load_dataset("csv", data_files="my_data.csv")
# ds = load_dataset("csv", data_files={"train": "train.csv", "test": "test.csv"})

# From JSON / JSONL
# ds = load_dataset("json", data_files="data.jsonl")


# From a Pandas DataFrame directly
# df = pd.read_csv("data.csv")
# ds = Dataset.from_pandas(df)

# From a Python dict
ds = Dataset.from_dict({
    "text":  ["Hello world", "Foo bar", "cuda"],
    "label": [1, 0, 0],
})
print(ds)