import torch

x = torch.arange(0, 100, 10)
print("x:", x)
print("x.dtype:", x.dtype)      # int64 -- this is the cause of the error

# min(), max() and sum() all worked on this tensor. mean() will not.
try:
    print("Mean:", x.mean())
except RuntimeError as error:
    print("\nx.mean() fails:")
    print("  ", error)

# Read the end of that message: "Got: Long".
