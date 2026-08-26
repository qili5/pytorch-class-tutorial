import torch

print("Right:", torch.tensor([3, 6, 9], dtype=torch.long).dtype)

float_tensor = torch.tensor([3.0, 6.0, 9.0])                # float32
int_tensor = torch.tensor([3, 6, 9], dtype=torch.int32)     # int32


print("\nOK: float32 * int32 =", float_tensor * int_tensor,
      "->", (float_tensor * int_tensor).dtype)

# --- Mismatch 1: matrix multiplication needs matching dtypes -------------
a32 = torch.rand(2, 2)
a16 = torch.rand(2, 2, dtype=torch.float16)

# torch.matmul(a32, a16)                            # this will error
# RuntimeError: expected m1 and m2 to have the same dtype,
#               but got: float != c10::Half
print("\n1. fix ->", torch.matmul(a32, a16.type(torch.float32)).dtype)

# --- Mismatch 2: writing a float result into an int tensor ---------------
# add_() with the trailing underscore writes back INTO int_tensor,
# and a float result does not fit in an int tensor.

# int_tensor.add_(float_tensor)                     # this will error
# RuntimeError: result type Float can't be cast to the desired output type Int
print("2. fix ->", int_tensor.type(torch.float32).add_(float_tensor))


