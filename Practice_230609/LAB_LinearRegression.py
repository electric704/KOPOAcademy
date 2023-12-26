## 선형회귀 구현된 모델 쓰지 않고 직접 만들어서 구현해보기
import torch

x_train = torch.FloatTensor([[1],[2],[3]])
y_train = torch.FloatTensor([[2],[4],[6]])

w = torch.zeros(1, requires_grad=True) ## 가중치 (Weight)초기화
b = torch.zeros(1, requires_grad=True) ## 편향 (bias)초기화

print(w)
print(b)

hypothesis = x_train * w + b
print(hypothesis)

cost = torch.mean((hypothesis - y_train) ** 2)
print(cost)

## 최적화 경사하강법 - 은 가져옴 ㅇㅇ
optimizer = torch.optim.SGD([w,b], lr = 0.01)

epochs = 2000
for epoch in range(epochs + 1):
    hypothesis = x_train * w + b

    cost = torch.mean((y_train - hypothesis) ** 2)

    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print('Epoch {:4d}/{} W: {:.3f}, b: {:.3f} Cost: {:.6f}'.format(
            epoch, epochs, w.item(), b.item(), cost.item()))
        
new_x = torch.Tensor([55])
new_y = new_x* w + b
print(new_y.item())



import torch 
import torch.nn as nn 
import torch.nn.functional as F


## 선형회귀 클래스 방식

torch.manual_seed(1)
# 데이터
x_train = torch.FloatTensor([[1], [2], [3]]) 
y_train = torch.FloatTensor([[2], [4], [6]])


## 반드시 nn.Module을 상속 받아야 작동한다.
class LinearRegressionModel(nn.Module): 
    def __init__(self): 
        super().__init__() 
        self.linear = nn.Linear(1, 1) # input: x_train.shape[-1]
    def forward(self, x): 
        return self.linear(x)

model = LinearRegressionModel()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01) 
epochs = 2000 

for epoch in range(epochs+1): 
    # H(x) 계산
    prediction = model(x_train) 
    # cost 계산
    cost = F.mse_loss(prediction, y_train) 
    optimizer.zero_grad() 
    cost.backward() 
    optimizer.step() 

if epoch % 100 == 0: 
    print('Epoch {:4d}/{} Cost: {:.6f}'.format( epoch, epochs, cost.item() ))