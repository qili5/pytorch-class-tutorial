import torch

# --- Mismatch 3: two different devices -----------------------------------
if torch.cuda.is_available():
    cpu_tensor = torch.tensor([3.0, 6.0, 9.0])
    gpu_tensor = torch.tensor([3.0, 6.0, 9.0]).to("cuda")
    print("\ncpu_tensor.device:", cpu_tensor.device,
          " gpu_tensor.device:", gpu_tensor.device)

    # print(" Not fix ->", (cpu_tensor + gpu_tensor).device)
    print("fix ->", (cpu_tensor.to("cuda") + gpu_tensor).device)
else:
    print("\n Device mismatch needs a GPU -- none available here.")