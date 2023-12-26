t = 100


def func_t():
    print('tennis')

class c_t:
    def __init__(self) -> None:
        self.t = 100

    def __call__(self):
        print('속성: ', self.t)