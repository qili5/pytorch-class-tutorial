import torch
# Tensor
TENSOR = torch.tensor([[[1, 2, 3],
                        [3, 6, 9],
                        [2, 4, 5]]])
print("TENSOR:\n", TENSOR)
print("Dimensions:", TENSOR.ndim)
print("Shape:", TENSOR.shape)
print("Size:", TENSOR.size())

