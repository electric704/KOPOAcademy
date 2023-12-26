## 다층 퍼셉트론 - 딥러닝은 XOR 문제를 풀 수 있다.
import torch
import torch.nn as nn

X = torch.FloatTensor([[0,0], [0,1], [1,0],[1,1]])
Y = torch.FloatTensor([[0],[1],[1],[0]])

model = nn.Sequential(
    nn.Linear(2, 10, bias=True),
    nn.Sigmoid(),
    nn.Linear(10, 10, bias=True),
    nn.Sigmoid(),
    nn.Linear(10, 10, bias=True),
    nn.Sigmoid(),
    nn.Linear(10, 1, bias=True),
    nn.Sigmoid()
)

criterion = torch.nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1)


for epoch in range(10001):
    optimizer.zero_grad()
    hypothesis = model(X)
    cost = criterion(hypothesis, Y)
    cost.backward()
    optimizer.step()
    if epoch % 100 == 0:
        print(epoch, cost.item())

hypothesis = model(X)
predicted = (hypothesis > 0.5).float()
accuracy = (predicted == Y).float().mean() * 100

print('모델의 출력값(Hypothesis): ', hypothesis)
print('모델의 예측값(Predicted): ', predicted)
print('실제값(Y): ', Y)
print('정확도(Accuracy): ', accuracy.item())

