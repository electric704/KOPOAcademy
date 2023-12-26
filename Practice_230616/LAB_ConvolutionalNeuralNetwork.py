import torch
import torch.nn as nn


# batch size × channel × height × width의 Tensor 선언
x = torch.full((1, 1, 5), 2.)
print(x)


# in_channels, out_channels, kernel_size, padding, stride
# 1d -> 1차원이라는 뜻
conv = nn.Conv1d(1, 1, 3, padding=0, stride=1)

## 여기가 가중치 선언부 3 x 3 크기를 1로 다 채움
## 상수로 채움
nn.init.uniform_(conv.weight, 1,1)
# nn.init.constant_(conv.weight, 1,1)
nn.init.uniform_(conv.bias, 3,3)



print(conv.weight, conv.bias)
print(conv(x))


# batch size × channel × height × width의 Tensor 선언
x = torch.full((1, 1, 5, 5), 2.)
print(x)
# in_channels, out_channels, kernel_size, padding, stride
conv = nn.Conv2d(1, 1, 3, padding=0, stride=1)
nn.init.uniform_(conv.weight, 1,1)
nn.init.uniform_(conv.bias, 3,3)
print(conv.weight, conv.bias)
print(conv(x))

# batch size × channel × height × width의 Tensor 선언
x = torch.full((1, 3, 5, 5), 2.)
print(x)
# in_channels, out_channels, kernel_size, padding, stride
conv = nn.Conv2d(3, 1, 3, padding=0, stride=1)
nn.init.uniform_(conv.weight, 1,1)
nn.init.uniform_(conv.bias, 3,3)
print(conv.weight, conv.bias)
print(conv(x))



# batch size × channel × height × width의 Tensor 선언
x = torch.full((1,3,5,5), 2. )
print(x)

# in_channels, out_channels, kernel_size, padding, stride
conv = nn.Conv2d(3,3,3, padding=0, stride=1)
nn.init.uniform_(conv.weight, 1, 1)
nn.init.uniform_(conv.bias, 3, 3)
print(conv.weight, conv.bias)

print(conv(x))

x = torch.full((1,1,5,5,5,), 2.)
print(x)

conv = nn.Conv3d(1,1,3, padding=0, stride=1)
nn.init.uniform_(conv.weight, 1, 1)
nn.init.uniform_(conv.bias, 3, 3)
print(conv.weight, conv.bias)

print(conv(x))