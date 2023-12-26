class AAA:
    def __init__(self) -> None:
        pass

a = 6

print(a)

f = AAA()

print(f)


########### 다중상속
class p1:
    def __init__(self):
        self.a = 100

class p2:
    def __init__(self):
        self.b = 200

class p3:
    def __init__(self):
        self.c = 300

class p4:
    def __init__(self):
        self.d = 400


class p5(p1, p2, p3, p4):
    def __init__(self):
        p1.__init__(self)
        p2.__init__(self)
        p3.__init__(self)
        p4.__init__(self)

pp = p5()
print(pp.a, pp.b, pp.c, pp.d)

## 맨앞에 녀석만 super로 초기화 - 파이선 2.0
class p6(p1, p2, p3, p4):
    def __init__(self):
        super().__init__()
        p2.__init__(self)
        p3.__init__(self)
        p4.__init__(self)

pp = p6()
print(pp.a, pp.b, pp.c, pp.d)


### 새로운 연산자 --- 생략하려고...;; 3.8 이상
a = 'Hello World'
b = len(a)
if b > 3:
    print('ok')    

## 위와 아래는 같은 코드임..
if b := len(a) > 3:
    print('ok')

## 함수 매개변수 순서 - 매개변수를 한 줄에 넣고 디폴트 초기화
def func ( a, b, c):
    a1 =a; b1 = b; c1 = c
    print(a1, b1, c1)
func(10, 20, 30)

def func(a, b, c = '100'):
    a1 = a; b1 = b; c1 =c
    print(a1, b1, c1)
func(10, 20, 30)
func(10, 20)
#func(10)

# 에러, 디폴트 초기화 오류
# def func(a, b='100', c):
#     a1 = a; b1 = b; c1 =c
#     print(a1, b1, c1)
# func(10, 20, 30)
    

## 가변인수 *로 표시
def func( a, b = '100', *c):
    print(a, b, c [0], c[1], c[2])
func(10, 20, 30, 40, 50)

def func( a, b = '100', *c):
    print(a, b, c)
func(10)

def func( a, b = '100', *c, d, **e):
    print(a, b, c, d, e)
## d = 60 안하면 구분 안 돼서 선언 해줘야함
func(10, 20, 30, 40, 50, d = 60, aa=1, bb=2, cc=3)

## 가변 인수를 딕셔너리로 받을 수 있음 대신 **로
data = {'aa':1, 'bb':2, 'cc':3}
func(10, 20, 30, 40, 50, d = 60, **data)


## 데코레이터
def deco1(func):
    def wrapper():
        print(func.__name__,'start')
        func()
        print(func.__name__, 'end')
    return wrapper

@deco1
def hello():
    print('hello')


#### 미니프로젝트
import numpy as np
import cv2 as cv
import random as rd

width = 1024
height = 600
depth =3

thickness = -1
offset_x = 50
offset_y = 20
x = 55
y = 22
screen_start_x = 100
screen_start_y = 500
bgr = (0, 255, 0)
count = 15

while(True):
    img = np.zeros(shape = (height, width, depth)) # img = npzeros((height, width, depth), np.uint8)

    for i in range(count):
        bar_cnt = rd.randint(1,6)

        for j in range(bar_cnt):
            start_x = screen_start_x + i * x
            start_y = screen_start_y - j * y
            cv.rectangle(img, (start_x, start_y), (start_x + offset_x, start_y + offset_y), bgr, thickness)

    cv.imshow("test", img)
    cv.waitKey(100)