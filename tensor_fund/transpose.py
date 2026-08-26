import torch

tensor_A = torch.tensor([[1, 2],
                          [3, 4],
                          [5, 6]], dtype=torch.float32)  # shape (3, 2)

tensor_B = torch.tensor([[7, 10],
                          [8, 11],
                          [9, 12]], dtype=torch.float32)  # shape (3, 2)

print("tensor_B shape:", tensor_B.shape)          # (3, 2)
print("tensor_B.T shape:", tensor_B.T.shape)      # (2, 3)

# Now (3, 2) @ (2, 3) is valid -> result is (3, 3)
print("tensor_A @ tensor_B.T:\n", torch.matmul(tensor_A, tensor_B.T))
