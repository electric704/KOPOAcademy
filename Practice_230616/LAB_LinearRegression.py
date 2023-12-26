## 선형회귀 구현된 모델 쓰지 않고 직접 만들어서 구현해보기
import torch
import torch.nn as nn
import torch.nn.functional as f


x_train = torch.FloatTensor([[1],[2],[3],[4],[5]])
y_train = torch.FloatTensor([[3],[5],[7],[9],[11]])

## linear regression
model = nn.Linear(1,1)

## 최적화 경사하강법 - 은 가져옴 ㅇㅇ
optimizer = torch.optim.SGD(model.parameters(), lr = 0.01)

epochs = 5000
for epoch in range(epochs + 1):
    prediction = model(x_train)

    cost = f.mse_loss(prediction, y_train) ## 예측 정답
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch % 1000 == 0:
        print('Epoch {:4d}/{} Cost: {:.6f}'.format(epoch, epochs, cost.item()))



        
new_x = torch.Tensor([15])
pred_y = model(new_x)
print(list(model.parameters()), pred_y)


x_train = torch.FloatTensor([[1,1], [2,2], [3,3], [4,4], [5,6], [7,7]])
y_train = torch.FloatTensor([[10], [15], [20], [25], [33], [40]])

model = nn.Linear(2, 1)
optimizer = torch.optim.SGD(model.parameters(), lr = 0.01)

epochs = 5000
for epoch in range(epochs + 1):
    prediction = model(x_train)
    cost = f.mse_loss(prediction, y_train)
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch % 1000 == 0:
        print('Epoch {:4d}/{} Cost: {:.6f}'.format(epoch, epochs, cost.item()))


new_x = torch.Tensor([6,8])
pred_y = model(new_x)
print(list(model.parameters()), pred_y)



x_train = torch.FloatTensor([[3,3,3], [4,4,4], [5,5,5], [6,6,6], [7,7,7]])
y_train = torch.FloatTensor([[6], [7], [8], [9],[10]])

model = nn.Linear(3, 1)
optimizer = torch.optim.SGD(model.parameters(), lr = 0.01)

epochs = 5000
for epoch in range(epochs + 1):
    prediction = model(x_train)
    cost = f.mse_loss(prediction, y_train)
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()
    
    if epoch % 1000 == 0:
        print('Epoch {:4d}/{} Cost: {:.6f}'.format(epoch, epochs, cost.item()))


new_x = torch.Tensor([11,3, 9])
pred_y = model(new_x)
print(list(model.parameters()), pred_y)
