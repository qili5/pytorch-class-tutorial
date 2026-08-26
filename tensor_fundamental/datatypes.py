import torch

# Create a float32 tensor
float_32_tensor = torch.tensor(
    [3.0, 6.0, 9.0],
    dtype=torch.float32
)

print("float32 tensor:", float_32_tensor)
print("Datatype:", float_32_tensor.dtype)

# Convert to float16
float_16_tensor = float_32_tensor.type(torch.float16)

print("\nfloat16 tensor:", float_16_tensor)
print("Datatype:", float_16_tensor.dtype)

# Convert to float64
float_64_tensor = float_32_tensor.type(torch.float64)

print("\nfloat64 tensor:", float_64_tensor)
print("Datatype:", float_64_tensor.dtype)

# Convert to integer
int_tensor = float_32_tensor.type(torch.int8)

print("\nint8 tensor:", int_tensor)
print("Datatype:", int_tensor.dtype)