data = [1,1,8,5,3]
print(data[3])
print(data[-3])
print(data[:])
print(data)
print(data[1:3])

data.append(3)
data.append(45)
data.append(125)
data.append(33)
data.append(18)
print(data)
data.sort()
print(data)
data.reverse()
print(data)


data = [0 for i in range(10)]
print(data)

data1 = ["kim", "Lee", "Seo", "Elsa", "Anna"]
print(data1)

data1 = [len(data) for i in data1]
print(data1)
data.clear()
print(data)

# 컴볼루션(합성곱) 계산
# data = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]
# mask = [2, 1, 3] -> 0, 1, 2이랑 곱해서 나온값 더함
# result = [7, 13, 19, 25, 25, 23, 17, 11]
# 식 = 0*2 + 1*1 + 2*3 = 7, 1*2 + 2*1 + 3*3 =13, 2*2 + 3*1 + 4*3 = 19

data = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]
mask = [2, 1, 3]
result = [
    (mask[0] * data[0+i]) + 
    (mask[1] * data[1+i]) + 
    (mask[2] * data[2+i]) for i in range(len(data) - 2)]
print(result)

data2 = [1,1,5,3,7,5]
#data2 = {1,1,5,3,7,5}
#data2 = (1,1,5,3,7,5)

for i in data2:
    print(data2)

data3 = {1:"a", 3:"b", 5:"c", 7:"d"}
for i in data3:
    #print(data3[i])
    print(data3.get(i))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
