import torch

x = torch.arange(0, 100, 10)
print("x:", x)
print("x.dtype:", x.dtype)      # int64 -- whole numbers

print("\nMinimum:", x.min())
print("Maximum:", x.max())
print("Sum:", x.sum())
print(f"Mean: {x.type(torch.float32).mean()}")

# x.min() and torch.min(x) are the same operation,
#  just two ways to write it.
print("\ntorch.min(x):", torch.min(x))
print("torch.max(x):", torch.max(x))
print("torch.sum(x):", torch.sum(x))
print("torch.mean(x.type(torch.float32)):", torch.mean(x.type(torch.float32)))

# Results print as tensor(90), not 90 -- still a tensor holding one value.
# Use .item() to pull out a plain Python number.
print("\nx.max() is:", x.max(), "-> type:", type(x.max()))
print("x.max().item() is:", x.max().item(), "-> type:", type(x.max().item()))
