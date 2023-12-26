class H():
    def __init__(self) -> None:
        print('H start')
    def test(self):
        print('H')

class A():
    def __init__(self) -> None:
        print('A start')
        print('A end')
    def test(self):
        print('A')

class B(H):
    def __init__(self) -> None:
        print('B start')
        print('B end')
    def test(self):
        print('B')

class C(H):
    def __init__(self) -> None:
        print('C start')
        super().test() ## D C B C B B
        print('C end')
    def test(self):
        print('C')

class D(C, B, A):
    def __init__(self) -> None:
        print('D start')
        super(D, self).__init__()
        super(C, self).__init__()
        ## H로 가려면
        #super(H, self).__init__()

result = D()
print(D.__mro__)