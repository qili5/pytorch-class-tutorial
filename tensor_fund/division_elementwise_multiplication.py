import torch

tensor = torch.tensor([1, 2, 3])
print("Original tensor:", tensor)

# Multiplication: multiplies every element by 10
print("Tensor * 10:", tensor * 10)
print("torch.multiply(tensor, 10):", torch.multiply(tensor, 10))

# Division: divides every element by 10
print("Tensor / 10:", tensor / 10)
print("torch.divide(tensor, 10):", torch.divide(tensor, 10))

# The original tensor is unchanged -- operations above weren't reassigned
print("Tensor after operations (unchanged):", tensor)

# Element-wise multiplication: each element multiplies its equivalent
print(tensor, "*", tensor)
print("Equals:", tensor * tensor)
