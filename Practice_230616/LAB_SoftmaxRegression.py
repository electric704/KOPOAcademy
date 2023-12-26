## 결과값이 여러 개의 값으로 결과가 나옴
import torch
import torch.nn as nn
import torch.nn.functional as f
import torch.optim as optim

torch.manual_seed(1)

x_train = [[1,2,1,1],
           [2,1,3,2],
           [3,1,3,4],
           [4,1,5,5],
           [1,7,5,5],
           [1,2,5,6],
           [1,6,6,6],
           [1,7,7,7]]

y_train = [2,2,2,1,1,1,0,0]
x_train = torch.FloatTensor(x_train)
y_train = torch.LongTensor(y_train)

print(x_train.shape)
print(y_train.shape)

W = torch.zeros((4,3), requires_grad=True)
b = torch.zeros((1,3), requires_grad=True)

optimizer = optim.SGD([W,b], lr=0.1)
epochs = 1000
for epoch in range(epochs+1):
    z = x_train.matmul(W) + b
    cost = f.cross_entropy(z, y_train)
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print('Epoch {:4d}/{} Cost: {:.6f}'.format
              (epoch, epochs, cost.item()))

print(z)



class SoftmaxClassifierModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(4,3)

    def forward(self, x):
        return self.linear(x)
    
model = SoftmaxClassifierModel()

optimizer = optim.SGD(model.parameters(), lr=0.1)
epochs = 1000

for epoch in range(epochs+1):
    prediction = model(x_train)
    cost = f.cross_entropy(prediction, y_train)
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print('Epoch {:4d}/{} Cost: {:.6f}'.format(epoch, epochs, cost.item()))


print(prediction)