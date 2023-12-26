g = 200


def func_g():
    print('golf')

class c_g:
    def __init__(self) -> None:
        self.g = 200

    def __call__(self):
        print('속성: ', self.g)

## 모듈인지 아닌지 체크하는 법
if __name__ == "__main__":
    pass
