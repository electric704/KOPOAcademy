class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

class Korean(Person):
    def __init__(self, age, name, city):
        super().__init__(age, name)
        self.city = city

class Student(Korean):
    def __init__(self, age, name, city, subject):
        super().__init__(age, name, city)
        self.subject = subject

a = Student(30, "kim", "Asan", "Python")
b = Student(25, "Lee", "Seoul", "Java")
c = Student(40, "Park", "Jeju", "AI")

print(Student.__mro__)

print(f"나이(Age): {a.age, b.age, c.age}")
print(f"이름(Name): {a.name, b.name, c.name}")
print(f"도시(City): {a.city, b.city, c.city}")
print(f"과목(Subject): {a.subject, b.subject, c.subject}")


## 슬롯은 잘 안쓰는 형태긴 하다.
## Class 변수는 Dict 형태로 저장된다.
## 따라서 파이썬에서는 클래스 변수를 선언하지 않아도
## 언제든지 추가할 수 있다.
class Student2(Korean):
    __slot__ = ("age", "name", "job")
    def __init__(self):
        self.age = ''

s2 = Student2()
s2.city = "Asan"
print(s2.__dict__.items())


class H():
    def __init__(self):
        print('H start')
    def test(self):
        print('H')

class A():
    def __init__(self):
        print('A start')
        print('A end')
    def test(self):
        print('A')

class B(H):
    def __init__(self):
        print('B start')
        # super().test()
        print('B end')
    def test(self):
        print('B')

class C(H):
    def __init__(self):
        print('C start')
        super().test()
        print('C end')
    def test(self):
        print('C')

class D(C, B, A):
    def __init__(self):
        print('D start')
        super(D, self).__init__()
        super(C, self).__init__()

result = D()
print(D.__mro__)



class aa():
    # cnt = 0
    def __init__(self):
        self.cnt = 0

    # @:classmethodd
    def add(self):
        self.cnt += 1

    ## 아래는 주석 같은 거 아님
    @staticmethod
    def substract(x1, x2):
        return x1 + x2

a1 = aa()
a2 = aa()
a3 = aa()

a1.add()
a2.add()
a3.add()

print(a1.cnt)
print(a1.substract(10,20))

## id --> 주솟값 찍기
print(id(a1))
print(id(a2))
print(id(a3))



a1 = aa()
print(id(a1))
a2 = aa()
print(id(a2))
a3 = aa()
print(id(a3))