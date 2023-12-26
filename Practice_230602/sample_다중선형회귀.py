import torch # 설치: pip install torch
# 확인: pip list
import torch.nn as nn
import torch.nn.functional as f

torch.manual_seed(1) # 생성하는 random number 고정
# 데이터셋 정의
x_train = torch.Tensor([[73, 80, 75], 
[93, 88, 93], 
[89, 91, 90], 
[96, 98, 100], 
[73, 66, 70]]) 
y_train = torch.Tensor([[152], [185], [180], [196], [142]])
# 모델 정의
model = nn.Linear(3, 1) # 모델 선언 및 초기화
# input_dim = 3, output_dim = 1

print(list(model.parameters())) # 첫번째값이 w, 두번째값이 b (랜덤 초기화)
# requires_grad=True : 학습의 대상
# 최적화 알고리즘 정의. 경사하강법 SGD, learning rate = 0.00001 (1e-5)
optimizer = torch.optim.SGD(model.parameters(), lr=0.00001)
# 학습. Cost가 0에 가까울수록 학습이 잘 된 것
epochs = 2000 # 1 에폭: 데이터셋을 1회 학습
for epoch in range(epochs + 1):
    prediction = model(x_train)
    cost = f.mse_loss(prediction, y_train) # 예측값 – 정답
    optimizer.zero_grad()
    cost.backward() # 기울기 구함
    optimizer.step()
    if epoch % 100 == 0:
        print('Epoch {:4d}/{} Cost: {:.6f}'.format(epoch, epochs, cost.item()))


# 예측(Prediction)
new_x = torch.Tensor([[73, 80, 75]])
pred_y = model(new_x)
print(pred_y)
print(list(model.parameters()))