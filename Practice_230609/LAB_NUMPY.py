
## numpy
import numpy as np

## 1 x 1
a = np.array([1,3,5])
b = np.array([4,2,0])
print(np.dot(a,b)) ## 내적
print(np.matmul(a,b)) ## 행렬곱

## 2 x 2
a = np.array([[1,3], [2,4]])
b = np.array([[1,0], [2,1]])
print(np.dot(a,b)) ## 내적
print(np.matmul(a,b)) ## 행렬곱

## 2 x 1
a = np.array([[1,3], [2,4]])
b = np.array([2,1])
print(np.dot(a,b)) ## 내적
print(np.matmul(a,b)) ## 행렬곱

## 1차원 x 스칼라
a = np.array([1,3,5])
b = 2
print(np.dot(a,b))
## 스칼라 행렬곱은 에러임
#  print(np.matmul(a,b))

## 2 x 3
a = np.array([[1,3],[2,4]])
b = np.array([[[1,1],[0,1]],[[5,0],[0,0]]])
print(a)
print(b)

## n x n
a = np.random.rand(9,8,5,13)
b = np.random.rand(9,8,13,3)
print(np.dot(a,b).shape)
print(np.matmul(a,b).shape)