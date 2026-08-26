import torch

x = torch.arange(0, 100, 10)
print("x:", x)
print("x.dtype:", x.dtype)      # int64 -- mean() cannot work with this

# The fix: convert to float32 (the most common dtype in PyTorch)
x_float = x.type(torch.float32)
print("x_float:", x_float)
print("x_float.dtype:", x_float.dtype)

# Now mean() works
print("\nMean:", x_float.mean())

# Usually written in one line
print("Mean (one line):", x.type(torch.float32).mean())

# Function form
print("torch.mean(x.type(torch.float32)):", torch.mean(x.type(torch.float32)))

# .type() returns a NEW tensor
print("\nx.dtype is still:", x.dtype)
