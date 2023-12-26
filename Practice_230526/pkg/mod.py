a= 100

def add(x1, x2):
    return x1 + x2

class calc():
    def mul(self, x1, x2):
        return x1 * x2
    
if __name__ == '__main__':
    ## 실행시키는 파일이 메인
    print("main")
else:
    ## 모듈 들어가면 이쪽임
    print("package module")