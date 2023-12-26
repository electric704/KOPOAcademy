## http://bigdata.dongguk.ac.kr/lectures/Python/_book/numpy.html
import numpy as np # numpy 패키지 로드하여 np로 사용


a = np.array([1,2,3])
b = np.array([[1, 2], [3,4]])
c = np.array([[[1,2],[3,4]], [[5,6], [7,8]]])
d = np.array([[1],[2],[3]], float)

print(type(a),a.shape, a.dtype)
print(type(b),b.shape, b.dtype)
print(type(c),c.shape, c.dtype)
print(type(d),d.shape, d.dtype)

a = [[1,2,3], [4,5,6]] # 리스트에서 행렬생성
b = np.array(a) 
print(a, b)
print(type(a), type(b))

## 242 사이즈
e = np.array([
    [[1,2], [3,4], [3,4], [3,4]],
    [[5,6], [7,8], [7,8], [7,8]]])
print(type(e),e.shape, e.dtype)

a = [[1,2,3],[4,5,6]]
b = np.array(a)
print(b)
print(b.shape)
print(b[0,0])

print(np.arange(10))
print(np.arange(5,10))
print(np.arange(5,15,3))
print(np.random.rand(2,3))
print(np.empty((2,3)))
print(np.zeros((2,3)))
print(np.ones((2,3)))
print(np.full((2,3),5))
print(np.eye(3))

a = np.arange(20)
b = a.reshape([4,5])

data = [[1,2,3], [4,5,6], [7,8,9]]
arr = np.array(data)
a = arr[0:2, 0:2]
print(a)
a = arr[1, 1]
print(a)


a = np.array([1,2,3])
b = np.array([4,5,6])

c = a+b
c = np.add(a,b)

c = a -b 
c = np.subtract(a,b)

c = a * b
c = np.multiply(a,b)

c = a / b
c = np.divide(a,b)

a = np.array([[1,2,3], [4,5,6]])
b = np.sum(a)
c = a.sum()
d = a.mean()

print(a)
print(c)
print(d)


a = np.arange(60)
b = a.reshape([4,5,3])
print(a)
print(b)
