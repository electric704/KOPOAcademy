s = 300


def func_s():
    print('soccer')

class c_s:
    def __init__(self) -> None:
        self.s = 300

    def __call__(self):
        print('속성: ', self.s)