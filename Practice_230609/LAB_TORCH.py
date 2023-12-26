import torch
## pip install torch
a = torch.Tensor([[1,2,3],[4,5,6]])
print(a, a.shape)
b = a.numpy()
a = torch.Tensor(a)

a = torch.IntTensor([[1,2,3],[4,5,6]])
a = torch.ShortTensor([[1,2,3],[4,5,6]])
a = torch.LongTensor([[1,2,3],[4,5,6]])
a = torch.FloatTensor([[1,2,3],[4,5,6]])
a = torch.DoubleTensor([[1,2,3],[4,5,6]])
a = torch.tensor([[1,2,3],[4,5,6]])

a = torch.arange(10)
a = torch.arange(5,10)
a = torch.arange(5,15,3)
a = torch.rand(2,3)
a = torch.empty(2,3)
a = torch.zeros(2,3)
a = torch.ones(2,3)
a = torch.full((2,3), 5)
a = torch.eye(2,3)


x = [1,2,3]
y = [2,4,6]
H = [1,2,3]

a = (((y[0] - H[0]))^2 + ((y[1] - H[1]))^2 + ((y[2] - H[2]))^2) / 3
print(a)


import torch.nn.functional as f
import torch.nn as nn

p = torch.Tensor([1,2,3,])
y = torch.Tensor([2,4,6,])
cost = torch.mean((p-y)**2)
cost2 = f.mse_loss(p,y)
print(cost)
print(cost2)
print(cost2.item())


## 선형 회귀(Linear Regression)
## 생성 랜덤 고정
torch.manual_seed(1)

## 데이터셋
x_train = torch.Tensor([[1], [2], [3]])
y_train = torch.Tensor([[2], [4], [6]])
print(type(x_train), x_train)
print(type(y_train), y_train)

## 모델 정의
model = nn.Linear(1, 1)
print(list(model.parameters()))

## 최적화 알고리즘, 경사 하강법, lr -> Learning Rate
optimizer = torch.optim.SGD(model.parameters(), lr = 0.01)

## 학습
epochs = 2000 # 1 에폭(epoch): 데이터 셋을 1회 학습, 단위
for epoch in range(epochs + 1):
    prediction = model(x_train)

    cost = f.mse_loss(prediction, y_train)
    optimizer.zero_grad() # 기울기 초기화
    cost.backward() # 기울기 구하는 공식, 한줄로 됌 ㅇㅇ
    optimizer.step()
    if epoch % 100 == 0:
        print('Epoch {:4d}/{} Cost: {:.6f}'.format(epoch, epochs, cost.item()))

## 예측
a = input()
new_x = torch.Tensor([[float(a)]])
pred_y = model(new_x)
print(pred_y)



## 다중 선형 회귀(Multivariate Linear Regression)
torch.manual_seed(1)

## 데이터셋 정의
x_train = torch.Tensor([[73, 80, 75],
                       [93, 88, 93],
                       [89, 91, 90],
                       [96, 98, 100],
                       [73, 66, 70]])
y_train = torch.Tensor([[152], [185], [180], [196], [142]])

## 모델 정의
## Linear 인자 값은 a차원에서 b차원으로 간다는 걸 명시함
## 현재 아래 경우에는 3차원에서 1차원으로 산출된다는 것을 명시
model = nn.Linear(3,1)
print(list(model.parameters()))

## 최적화 함수 -> SGD 경사하강법, Learning Rate = 0.00001
optimizer = torch.optim.SGD(model.parameters(), lr=0.00001)

## 반복학습, Cost가 0에 수렴할수록 학습 잘 됌
epochs = 2000
for epoch in range(epochs+1):
    prediction = model(x_train)

    cost = f.mse_loss(prediction, y_train) ## 예측 정답
    optimizer.zero_grad() ## 초기화 - optimizer에 계산된 기울기가 초기화 되지 않아서 따로 해야함
    cost.backward() ## 기울기 구함
    optimizer.step() ## 진행

    ## 학습 중 출력
    if epoch % 100 == 0:
        print('Epoch {:4d}/{} Cost: {:.6f}'.format(epoch, epochs, cost.item()))

## 예측
new_x = torch.Tensor([[73, 80, 75]])
pred_y = model(new_x)
print(pred_y)
print(list(model.parameters()))