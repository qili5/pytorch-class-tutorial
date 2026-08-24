import torch
tensor_A = torch.tensor([[1, 2],
                          [3, 4],
                          [5, 6]], dtype=torch.float32)  # shape (3, 2)

tensor_B = torch.tensor([[7, 10],
                          [8, 11],
                          [9, 12]], dtype=torch.float32)  # shape (3, 2)

print("tensor_A shape:", tensor_A.shape)
print("tensor_B shape:", tensor_B.shape)

print(torch.matmul(tensor_A, tensor_B))

