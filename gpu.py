import torch
print(torch.cuda.is_available())  # 应为 True
print(torch.cuda.device_count())  # 应 >= 1
print(torch.cuda.get_arch_list())   # 应包含 'sm_120'