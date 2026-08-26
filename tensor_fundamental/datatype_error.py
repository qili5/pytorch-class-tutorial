import torch

print("Right:", torch.tensor([3, 6, 9], dtype=torch.long).dtype)

float_tensor = torch.tensor([3.0, 6.0, 9.0])                # float32
int_tensor = torch.tensor([3, 6, 9], dtype=torch.int32)     # int32

print("\nOK: float32 * int32 =", float_tensor * int_tensor,
      "->", (float_tensor * int_tensor).dtype)

# print("matmul float32 @ int32 =",
#       torch.matmul(float_tensor, int_tensor))

# Convert one side and it works:
print("fix ->: matmul float32 @ int32 =",
      torch.matmul(float_tensor, int_tensor.type(torch.float32)))

a32 = torch.rand(2, 2)
a16 = torch.rand(2, 2, dtype=torch.float16)

# print("\n1. Mismatch ->", torch.matmul(a32, a16).dtype)
# Convert one side and it works:
print("\n fix ->", torch.matmul(a32, a16.type(torch.float32)))

# print("2. fix ->", int_tensor.add_(float_tensor))
# Convert one side and it works:
print("fix ->", int_tensor.type(torch.float32).add_(float_tensor))


