## 이전에 한 모델들에서 시그모이드가 붙은 것 뿐

import torch
import torch.nn as nn

X = torch.FloatTensor([[0,0], [0, 1], [1,0], [1,1]])
## 아래는 XOR 모델
## Y = torch.FloatTensor([[0],[1],[1],[0]])
Y = torch.FloatTensor([[1],[0],[0],[1]])

## 이 층이 여러 개면 딥뉴럴네트워크
linear = nn.Linear(2, 1, bias=True)
sigmoid = nn.Sigmoid() ## 추가되는 상황
model = nn.Sequential(linear,sigmoid)

criterion = torch.nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1)


## 여러 개의 층을 학습시키면 딥러닝
for step in range(10001):
    optimizer.zero_grad()
    hypothesis = model(X)
    cost = criterion(hypothesis, Y)
    cost.backward()
    optimizer.step()

    if step % 100 == 0:
        print(step, cost.item())

hypothesis = model(X)
predicted = (hypothesis > 0.5).float()
accuracy = (predicted == Y).float().mean() * 100
print('모델의 출력값(Hypothesis): ', hypothesis)
print('모델의 예측값(Predicted): ', predicted)
print('실제값(Y): ', Y)
print('정확도(Accuracy): ', accuracy.item())

## 위 퍼셉트론은 XOR 문제를 풀 수 없다 이유는
## XOP의 구분은 그래프나 행렬 상에서 선 하나로 구분 지을 수 없기 때문에
## 선형회귀 역시 XOR을 쓸 수 없다.