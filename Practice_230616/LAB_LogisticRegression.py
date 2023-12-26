## 결과값이 0 혹은 1임 이진 식으로 결과가 나옴

import torch
import matplotlib.pyplot as plt 

def sigmoid(x):
    return 1 / (1 + torch.exp(-x))
x = torch.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(0.5 * x)
y2 = sigmoid(x)
y3 = sigmoid(2 * x)
y4 = sigmoid(10 * x)
plt.plot(x, y1, 'r', linestyle='--') # w = 0.5
plt.plot(x, y2, 'g') # w = 1
plt.plot(x, y3, 'b', linestyle='--') # w = 2
plt.plot(x, y4, 'black', linestyle='--') # w = 10
plt.plot([0,0],[1.0,0.0], ':') # 가운데 점선 추가
plt.title('Sigmoid Function')
plt.show()


def sigmoid(x):
    return 1 / (1 + torch.exp(-x))
x = torch.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(x + 0.5)
y2 = sigmoid(x)
y3 = sigmoid(x + 1.0)
y4 = sigmoid(x + 2.0) ## 위 수식 비교해 수치값 조정
plt.plot(x, y1, 'r', linestyle='--')
plt.plot(x, y2, 'g')
plt.plot(x, y3, 'b', linestyle='--')
plt.plot(x, y4, 'black', linestyle='--')
plt.plot([0,0],[1.0,0.0], ':')
plt.title('Sigmoid Function')
plt.show()


import torch
import torch.nn as nn
import torch.nn.functional as f
import torch.optim as optim

torch.manual_seed(1)

torch.manual_seed(1)
x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]] #다중로지스틱회귀
#x_data = [[1], [2], [3], [4], [5], [6]] # 로지스틱회귀
y_data = [[0], [0], [0], [1], [1], [1]] 
x_train = torch.FloatTensor(x_data) 
y_train = torch.FloatTensor(y_data)
model = nn.Sequential( 
nn.Linear(2, 1), # 다중로지스틱회귀
# nn.Linear(1, 1), # 로지스틱회귀
# nn.Linear(1, 1, bias=False), # 편향 사용 여부
nn.Sigmoid()
)


model(x_train)
optimizer = optim.SGD(model.parameters(), lr=0.1) 
epochs = 5000 


for epoch in range(epochs + 1):
    hypothesis = model(x_train)
    cost = f.binary_cross_entropy(hypothesis, y_train)
    # cost = f.mse_loss(hypothesis, y_train) # 선형회귀
    optimizer.zero_grad() 
    cost.backward()
    if epoch % 10 == 0: 
        prediction = hypothesis >= torch.FloatTensor([0.5]) 
        correct_prediction = prediction.float() == y_train 
        accuracy = correct_prediction.sum().item() / len(correct_prediction) 
        print('Epoch {:4d}/{} Cost: {:.6f} Accuracy {:2.2f}%'.format(
            epoch, epochs, cost.item(), accuracy * 100, ))
model(x_train)
print(list(model.parameters()))



x_data = [[1,2],[2,3],[3,1],[4,3],[5,3],[6,2]]
y_data = [[0],[0],[0],[1],[1],[1]]

x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)

class BinaryClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(2,1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        return self.sigmoid(self.linear(x))

model = BinaryClassifier()

optimizer = optim.SGD(model.parameters(), lr=0.1)
epochs = 5000

for epoch in range(epochs + 1):
    hypothesis = model(x_train)
    cost = f.binary_cross_entropy(hypothesis, y_train)
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch % 10 == 0:
        prediction = hypothesis >= torch.FloatTensor([0.5])
        correct_prediction = prediction.float() == y_train
        accuracy = correct_prediction.sum().item() / len(correct_prediction)
        print('Epoch {:4d}/{} Cost: {:.6f} Accuracy {:2.2f}%'.format(
            epoch, epochs, cost.item(), accuracy * 100, ))
        
model(x_train)
print(list(model.parameters()))
