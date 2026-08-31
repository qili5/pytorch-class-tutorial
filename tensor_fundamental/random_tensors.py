import torch
# Create a random tensor of size (3, 4)
random_tensor_1value = torch.rand(4)
print("Random tensor with 1 value:\n", random_tensor_1value)

random_tensor = torch.rand(size=(3, 4))
print("random_tensor dim", random_tensor.ndim)
print("Random tensor:\n", random_tensor)
print("Random tensor dtype:", random_tensor.dtype)

# Create a random tensor of size (224, 224, 3) -> height, width, color_channels
random_image_size_tensor = torch.rand(size=(224, 224, 3))
print("random_image_size_tensor dim", random_image_size_tensor.ndim)
print("Random image size tensor shape:", random_image_size_tensor.shape)
print("Random image size tensor ndim:", random_image_size_tensor.ndim)
