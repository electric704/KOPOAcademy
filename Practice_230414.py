def unit_step_func(x):
    if x >= 0:
        return 1
    else:
        return 0
    
y = unit_step_func(2.5)
print(y)


##################### 배열 선언하면서 세팅

data1 = [i for i in range(10)]
data2 = list(i for i in range(10))
data3 = [i for i in range(20) if i % 3 == 0]
data4 = [i*j for j in range(5) for i in range(2)]

data5 = [i*j for j in range(2, 10) for i in range(1, 10)]

print(data1, data2, data3, data4, data5)

################################ 이중문 조건

data1 = [i * j for j in range (2, 10) for i in range(1,10)]
data1 = [i* j for j in range(2, 10 ) for i in range(1, 10)]
data2 = [i for i in range(20) if i % 2 == 0 or i % 3 == 0]

print( data1, data2)

################ 다른 자료형 한번에 선언세팅
#### 이차배열
data1 = [[i + j for i in range(2)] for j in range(5)]

#### dict
data2 = {str(i) : i for i in range(5)}

#### set
data3 = {i for i in range(5)}

#### tuple (형변환)
data4 = tuple(i for i in range(5))
print(type(data4))

#### generator expression --- 안하면 형변환 안 되고 걍 제네레이터임;;
data4 = (i for i in range(5))
print(type(data4))

#### 갑분 예제
a = 100

while(True):
    a -= 1
    if a == 50:
        break

print(a)


#### Class 사용 및 제작
class person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class person2:
    def __init__(self, addr):
        self.addr = addr
        
class student(person1, person2):
    def __init__(self, name, gender, job = "student"):
        super().__init__(name, job)
        self.gender = gender
        self.job = job

p1 = person1("Lotus", 31)
p2 = person2("천안")
s1 = student("Lotus", "F")

print(type(p1), type(p2), type(s1))
print(p1.age, p2.addr, s1.gender, s1.job)



#### 인덱싱 비어있을 땐 append해야함

data = []
data.append(10)
data.append(20)
data.append(30)
print(data[0], data[1], data[2])
data.clear()

data = [0, 0, 0]
data.append(10)
data.append(20)
data.append(30)
print(data[0], data[1], data[2])
data.clear()

a = person1
a1 = a("Cosmo", 5)
print(a1.name)


#### 일급 객체 함수 배열화
class calc1():
    def add(self, x1, x2):
        return x1 + x2
    
class calc2():
    def sub(self, x1, x2):
        return x1 - x2
    
c1 = calc1()
c2 = calc1()
c3 = calc2()
c4 = calc2()

## 배열화
data = [c1, c2, c3, c4]
print(data[0].add(10, 5))
print(data[1].add(10, 5))
print(data[2].sub(10, 5))
print(data[3].sub(10, 5))

## dict화
data = {'1': c1, '2': c2, '3': c3, '4': c4}
print(data['1'].add(10, 5))
print(data['3'].sub(10, 5))

def calc(x1, x2):
    return x1 + x2, x1 - x2, x1 * x2, x1 / x2

print(calc(3, 5))
print(type(calc(3, 5)))

#### 함수 내 함수
def square(x1):
    return x1 * x1

def power(func, n):
    return func(n)

power(square, 5)


def calc():
    def add(x1, x2):
        y = x1 + x2
        return y
    return add

c = calc
print(c()(3, 5))