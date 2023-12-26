import numpy as np
a = np.array([1, 2, 3])
b = np.array([[1., 2], [3, 4]])
c = np.array([[[1, 2], [3, 4]],[[5,6],[7,8]]])
d = np.array([[1],[2],[3]], float)
e = np.array([
    [[1],[2],[3],[4],[5]],
    [[6],[7],[8],[9],[10]]])

print(type(a), a.shape, a.dtype)
print(type(b), b.shape, b.dtype)
print(type(c), c.shape, c.dtype)
print(type(d), d.shape, d.dtype)
print(type(e), e.shape, e.dtype)


a = [[1,2,3], [4,5,6]]
b = np.array(a)
print(b)
print(b.shape)
print(b[0,0])

print(np.arange(10))
print(np.arange(5, 10))
print(np.arange(5, 15, 3))
print(np.random.rand(2,3))
print(np.empty((2,3)))
print(np.zeros((2,3)))
print(np.ones((2,3)))
print(np.full((2,3),5))
print(np.eye(3))


import threading
import time

def NumSum(a):
    while True:
        time.sleep(5)
        sum = 0
        for i in range(0, a + 1):
            sum += i
        print('10까지 합계: ', sum)

t = threading.Thread(target=NumSum, args=(100, ))
t.start()

while True:
    age = input("나이: ")
    print(age)
    sum = 0
    for i in range (1, 100):
        sum += i
    print(sum)