import torch

tensor = torch.tensor([1, 2, 3])

# Element-wise multiplication (for comparison): [1*1, 2*2, 3*3]
print("Element-wise:", tensor * tensor)

# Matrix multiplication (dot product): (1*1) + (2*2) + (3*3)
print("Matrix multiplication (torch.matmul):", torch.matmul(tensor, tensor))

# The @ symbol is shorthand for torch.matmul()
print("Matrix multiplication (@ operator):", tensor @ tensor)

# Now with an actual 2D array (matrix) instead of a 1D vector
matrix_a = torch.tensor([[1, 2],
                          [3, 4]])
matrix_b = torch.tensor([[5, 6],
                          [7, 8]])
print("matrix_a:\n", matrix_a)
print("matrix_b:\n", matrix_b)

print("Element-wise:\n", matrix_a * matrix_b)

print("Matrix multiplication (torch.matmul):\n", torch.matmul(matrix_a, matrix_b))

print("Matrix multiplication (@ operator):\n", matrix_a @ matrix_b)
tensor_a = torch.rand(size=(3, 2))
tensor_b = torch.rand(size=(2, 3))
print("tensor_a shape:", tensor_a.shape)
print("tensor_b shape:", tensor_b.shape)
print("tensor_a @ tensor_b shape:", (tensor_a @ tensor_b).shape)
