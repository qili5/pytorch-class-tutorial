import torch

tensor = torch.arange(10, 100, 10)
print(f"Tensor: {tensor}")

# argmax/argmin give the POSITION of the value, not the value itself
print(f"Index where max value occurs: {tensor.argmax()}")
print(f"Index where min value occurs: {tensor.argmin()}")

# Feed that index back into the tensor to get the value
print(f"\nValue at max index: {tensor[tensor.argmax()]}")
print(f"Compare with tensor.max(): {tensor.max()}")

# Function form works too
print(f"\ntorch.argmax(tensor): {torch.argmax(tensor)}")
print(f"torch.argmin(tensor): {torch.argmin(tensor)}")
