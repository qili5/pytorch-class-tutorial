import torch

# Create a range of values 0 to 10 (end is exclusive -> stops at 9)
zero_to_ten = torch.arange(start=0, end=10, step=1)
print("Zero to ten:", zero_to_ten)

# Create a tensor of zeros with the same shape as another tensor
ten_zeros = torch.zeros_like(input=zero_to_ten)
print("Ten zeros (same shape as zero_to_ten):", ten_zeros)

# Create a tensor of ones with the same shape as another tensor
ten_ones = torch.ones_like(input=zero_to_ten)
print("Ten ones (same shape as zero_to_ten):", ten_ones)
