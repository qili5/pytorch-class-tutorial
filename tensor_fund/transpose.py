import torch

tensor_A = torch.tensor([[1, 2],
                          [3, 4],
                          [5, 6]], dtype=torch.float32)  # shape (3, 2)

tensor_B = torch.tensor([[7, 10],
                          [8, 11],
                          [9, 12]], dtype=torch.float32)  # shape (3, 2)

# tensor_A (3, 2) @ tensor_B (3, 2) fails -- inner dimensions (2 and 3) don't match.
# Fix: make the inner dimensions match using a transpose (swap a tensor's dimensions)
# Two equivalent ways to transpose:
#   torch.transpose(input, dim0, dim1)
#   tensor.T
print("tensor_B shape:", tensor_B.shape)          # (3, 2)
print("tensor_B.T shape:", tensor_B.T.shape)      # (2, 3)

# Now (3, 2) @ (2, 3) is valid -> result is (3, 3)
print("tensor_A @ tensor_B.T:\n", torch.matmul(tensor_A, tensor_B.T))
