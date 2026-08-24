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

# Element-wise multiplication (for comparison): each position multiplies its equivalent
# [[1*5, 2*6],
#  [3*7, 4*8]]
print("Element-wise:\n", matrix_a * matrix_b)

# Shape rule (compatibility): columns of the 1st matrix must equal rows of the 2nd matrix
# matrix_a is (2, 2), matrix_b is (2, 2) -> 2 == 2, so this is valid
#
# Calculation rule: each output value = (a row from matrix_a) dotted with (a column from matrix_b)

print("Matrix multiplication (torch.matmul):\n", torch.matmul(matrix_a, matrix_b))

# The @ symbol is shorthand for torch.matmul()
print("Matrix multiplication (@ operator):\n", matrix_a @ matrix_b)

# Shape rule, generalized: (m, n) @ (n, p) -> (m, p)
# The inner dimensions (n, n) must match; the result takes the outer dimensions (m, p)
# (3, 2) @ (2, 3) is valid because the inner dimensions (2, 2) match -> result is (3, 3)
# (3, 2) @ (3, 4) would NOT be valid because 2 != 3
tensor_a = torch.rand(size=(3, 2))
tensor_b = torch.rand(size=(2, 3))
print("tensor_a shape:", tensor_a.shape)
print("tensor_b shape:", tensor_b.shape)
print("tensor_a @ tensor_b shape:", (tensor_a @ tensor_b).shape)
