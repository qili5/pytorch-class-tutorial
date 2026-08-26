import torch

tensor = torch.tensor([1, 2, 3])
print("Original tensor:", tensor)

# Addition: adds 10 to every element
print("Tensor + 10:", tensor + 10)
print("torch.add(tensor, 10):", torch.add(tensor, 10))

# Subtraction: subtracts 10 from every element
print("Tensor - 10:", tensor - 10)
print("torch.subtract(tensor, 10):", torch.subtract(tensor, 10))

# The original tensor is unchanged -- operations above weren't reassigned
print("Tensor after operations (unchanged):", tensor)

# To actually change it, reassign the result
tensor = tensor + 10
print("Tensor after reassignment:", tensor)
