class Person:
    def __init__(self, name, age):
    #def __init__(self, name, age = 20):
        self.name = name
        self.age = age
        self.job = "student"

    def add(self, num):
        self.age += num
        return self.age
    
    def __del__(self):
        print("Person destructor")



p1 = Person("John", 36)
print(p1.name, p1.age, p1.job)
print(p1.add(30))


class avatar:
    def __init__(self, b, c = 'test'):
        self.a = 100
        self.b = b
        self.c = c

    def __del__(self):
        print("avatar destructor")

    def _test_(self):
        print("test")

class avatar2(avatar):
    def _test2_(self):
        self._test_()

    def __del__(self):
        print("avatar2 destructor")

a1 = avatar(32, 39)
a2 = avatar2(99, 99)

print(a1.a, a1.b, a1.c)
a2._test2_()

class avatar3:
    _special_item = 2

    def check_item(self):
        print(self._special_item)

a3 = avatar3()
a3.check_item()

print(a3._special_item)
print(avatar3._special_item)


class Person2:
    def add1(a,b):
        return a + b
    
    def add2(self, a, b):
        return a + b
    
    def __call__(self): # 걍 클래스 부르면 가동됌 -- a = A(), a()-> 식으로
        print("call")
    
p2 = Person2()

print(p2.add2(100, 50))
# print(p2.add1(100, 50)) -- ERROR # 인스턴스 지치이 없어 전역함수 사용이라 그냥 사용 못함

print(Person2.add1(100, 50)) # 인스턴스가 없으므로 클래스 내 전역 함수를 사용
# print(Person2.add2(100, 50)) -- ERROR # 이녀석은 인스턴스를 사용하기로 했기에 일반함수를 사용
print(Person2.add2(p2, 100, 50)) # 인스턴스를 사용하는데 굳이 전역함수로 쓰려면 앞에 인스턴스를 넣어주어야함
p2()
      
class Person3:
    def add1(self, a,b):
        return a+b
    
    def add2(self, a, b):
        return a + b
    
class Student1(Person3):
    def add2(self, a, b):
        return a * b

p3 = Person3()
S1 = Student1()

print(p3.add1(10, 5), S1.add1(10, 5))
print(p3.add2(10, 5), S1.add2(10, 5))


class tiger1:
    def cry(self):
        print("tiger1 cry")

    def eat(self):
        print("tiger1 eat")

class lion1:
    def cry(self):
        print("lion1 cry")

    def move(self):
        print("lion1 move")

class liger1(tiger1, lion1):
    pass

lg1 = liger1()
lg1.cry() # 다중 상속 시 같은 메소드일 경우 먼저 상속 받은 클래스 꺼 씀
lg1.move()


from abc import *  # abstract base class -> 추상클래스 ㄷㄷ

class testABC(metaclass=ABCMeta):
    @abstractmethod
    def testMothod(self):
        print("testing")



from math import *

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

pt1 = Point(3, 6, 0)
pt2 = Point(12, 2, 0)

print(sqrt((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2))

pt1 = Point(2, 6, 4)
pt2 = Point(5, 2, 8)

print(sqrt((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2 + (pt1.z - pt2.z) ** 2))



pt1 = [5,3,2,6,3,7,1,4,3]
pt2 = [8,1,4,7,3,5,5,4,8]

sum = 0
for i in range(len(pt1)):
    sum += (pt1[i] - pt2[i]) ** 2
    
print(sqrt(sum))


p1 = [2, 6]
p2 = [4, 12]
p3 = [6, 3]

# 분모
def Bummo(A, B):
    sum1 = 0
    sum2 = 0
    for i in range(len(A)):
        sum1 += A[i]
        sum2 += B[i]

    return sum1 * sum2

# 분자
def Bunza(A, B):
    sum = 0
    for i in range(len(A)):
        sum += A[i] * B[i]

    return sum

def PointToVector(p1, p2):
    vector = list(range(len(p1)))
    for i in range(len(p1)):
        vector[i] = p2[i] - p1[i]

    return vector

#print(Bunza([2, 6], [4, 3]) / Bummo([2, 6], [4, 3]))

print("코사인 유사도")

p1 = [2,6,4,3,8]
p2 = [5,2,8,1,2]

print(Bunza(p2, p1)/ Bummo(p2, p1))


import matplotlib.pyplot as plt

x = [10,20,30,40,50]
y = [10,20,30,40,50]
area = [100,200,300,400,500]
Colors = ['red', '#332266', 'yellow', '#6f6f6f', 'blue']

plt.figure(figsize=(10, 10))
plt.scatter(x,y,s=area, alpha=0.5, c= Colors)
plt.show()
