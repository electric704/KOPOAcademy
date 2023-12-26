import torch

a = torch.Tensor([[1,2,3],[4,5,6]])
print(a, a.shape)
b= a.numpy()
a = torch.Tensor(a)

a = torch.IntTensor([[1, 2, 3], [4, 5, 6]]) # int32 (class)
a = torch.ShortTensor([[1, 2, 3], [4, 5, 6]]) # int16 (class)
a = torch.LongTensor([[1, 2, 3], [4, 5, 6]]) # int64 (class)
a = torch.FloatTensor([[1, 2, 3], [4, 5, 6]]) # float32 (class)
a = torch.DoubleTensor([[1, 2, 3], [4, 5, 6]]) # float64 (class)
a = torch.tensor([[1, 2, 3], [4, 5, 6]]) # int (function)
a = torch.arange(10)
a = torch.arange(5, 10)
a = torch.arange(5, 15, 3)
a = torch.rand(2, 3)
a = torch.empty(2, 3)
a = torch.zeros(2, 3)
a = torch.ones(2, 3)
a = torch.full((2, 3), 5)
a = torch.eye(2, 3)

squeeze_tensor = torch.rand(size=(2,1,2,1,2)) 
print(squeeze_tensor.shape) # squeeze_tensor
print(squeeze_tensor.squeeze().shape) # (2, 2, 2)
print(squeeze_tensor.squeeze(3).shape) # (2, 1, 2, 2)
print(a.size())
print(a.ndimension())

unsqueeze_tensor = torch.rand(size=(2,2))
print(unsqueeze_tensor.shape) # unsqueeze_tensor
print(unsqueeze_tensor.unsqueeze(0).shape) # [1,2,2]
print(unsqueeze_tensor.unsqueeze(1).shape) # [2,1,2]
print(unsqueeze_tensor.unsqueeze(2).shape) # [2,2,1]


a = torch.Tensor([[1,2,3],[4,5,6]])
b = a.reshape(2, 3)
print(b)
c = a.flatten()
print(c)

a = torch.Tensor([[[1,2,3],[4,5,6]],
                  [[1,2,3],[4,5,6]],
                  [[1,2,3],[4,5,6]],
                  [[1,2,3],[4,5,6]]])
b = a.reshape(2,2,3,2) 
print(b)
c = a.flatten()
print (c)

# -> 비용함수, (예측값 - 정답(삽입값))제곱의 평균
prediction = torch.Tensor([1,2,3,4]) # 예측값 - 이게 나와야 정답예측
y_train = torch.Tensor([2,4,6,8])    # 삽입값 - 이게 지금 넣는 값(오차있음)
cost = torch.mean((prediction - y_train) ** 2) 
print(cost.item()) # item -> 텐서가 요소 하나로 되어있을 때 가져오는 키워드
# -> 손실함수, 제곱이 함수 안에서 구현됨
import torch.nn.functional as f
cost2 = f.mse_loss(prediction, y_train) # 예측값 – 정답
print(cost2.item())



import torch # 설치: pip install torch
# 확인: pip list
import torch.nn as nn
import torch.nn.functional as f
torch.manual_seed(1) # 생성하는 random number 고정

# 데이터셋 정의
# (입력값, 정답(Ground Truth))
# (1, 2), (2, 4), (3, 6)
x_train = torch.Tensor([[1], [2], [3]])
y_train = torch.Tensor([[2], [4], [6]])
print(type(x_train), x_train)
print(type(y_train), y_train)


# 모델 정의
model = nn.Linear(1, 1) # 모델 선언 및 초기화
# input_dim = 1, output_dim = 1
print(list(model.parameters())) # 첫번째값이 w, 두번째값이 b (랜덤 초기화)
# requires_grad=True : 학습의 대상
# 최적화 알고리즘 정의. 경사하강법 SGD, learning rate = 0.01
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
# 학습. Cost가 0에 가까울수록 학습이 잘 된 것
epochs = 2000 # 1 에폭: 데이터셋을 1회 학습
for epoch in range(epochs + 1):
    prediction = model(x_train)
    cost = f.mse_loss(prediction, y_train) # 예측값 – 정답
    optimizer.zero_grad()
    cost.backward() # 기울기 구함
    optimizer.step() # 가중치 업데이트 (w – 학습률 x 기울기)
    if epoch % 100 == 0:
        print('Epoch {:4d}/{} Cost: {:.6f}'.format(epoch, epochs, cost.item()))
# 예측(Prediction)
while True:
    a=input()
    new_x = torch.Tensor([[float(a)]])
    pred_y = model(new_x)
    print(pred_y)

