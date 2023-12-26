class A():
    def __init__(self) -> None:
        print('A start')
        super().__init__()
        print('A end')
    def test(self):
        print('A')

class B():
    def __init__(self) -> None:
        print('B start')
        super().__init__()
        print('B end')
    def test(self):
        print('B')  ## 오버라이딩

class C():
    def __init__(self) -> None:
        print('C start')
        super().__init__()
        print('C end')
    def test(self):
        print('C')  ## 오버라이딩

class D(C, B, A):
    def __init__(self) -> None:
        print('D start')
        super().__init__()
        # C: super().test()
        # A: super(B, self),test()
        # B: B.test(test)
        print('D end')

result = D()
result.test()       ## 최종적으로 C가 오버라이딩한 형태
print(D.__mro__)    ## mro 메소드 결정 순서


# 죽음의 다이아몬드
class A():
    pass

class B(A):
    def __init__(self) -> None:
        self.test1 = 'a1'
    pass

class C(A):
    def __init__(self) -> None:
        self.test2 = 'a2'
    pass

class D(A):
    def __init__(self) -> None:
        self.test3 = 'a3'
    pass

class E(D, C, B):
    def __init__(self) -> None:
        super(A, self).__init__()
        super(B, self).__init__()
        super(C, self).__init__()
        super(D, self).__init__()
        self.test4 = 'a4'
    pass

print(E.mro())
print(E().test2)

class A():
    def __init__(self) -> None:
        self.a = 100

class B(A):
    def __init__(self) -> None:
        A.__init__(self)
        print(self.a)

B()


class A():
    def __init__(self, a) -> None:
        print('A start')
        super().__init__()
        print('A end')
    def test(self):
        print('A')

class B():
    def __init__(self, a) -> None:
        print('B start')
        print('B end')
    def test(self):
        print('B')

class C():
    def __init__(self, a, b) -> None:
        print('C start')
        print('C end')
    def test(self):
        print('C')

class D(C, B, A):
    def __init__(self) -> None:
        print('D start')
        print('D end')

        ## 각 부모 클래스 초기화
        ## 개인적으로 이 방법이 더 직관적인듯
        ## {부모클래스}.__init__() --> ㅇㅇㅇ
        C.__init__(self, 30, 'b')
        B.__init__(self, 'B')
        A.__init__(self, 5)

result = D()
result.test()
print(D.__mro__)



class A():
    cnt = 0

a = A(); b = A(); c = A()
a.cnt = 100; b.cnt = 200; c.cnt = 300

A.cnt = 100

## A.cnt 는 공통으로 쓰는 것이고
## 나머지는 따로 쓰는 것
## 허나 이렇게 쓰면 엉망징창이 될 수 있음
print(A.cnt, a.cnt, b.cnt, c.cnt)
print(a.__dict__.items())
print(A.__dict__.items())