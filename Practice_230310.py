
'''
이거슨 주석이당
이거슨 주석이다용
이거슨 주석이래용!!
주우서서서서강
주주주우ㅜ우주ㅜ수서서걱
'''

# 한 줄에... 주석 하나...

print("hello")
print("hello " + "world")
print(("hello " + "world! ") * 3)
print(65)
print("C:\\python")
print("hello \"123\" world")

print("hello " + str(123) + " world")
print("hello " + "123" + " world")
print("hello", 123, "world"),
print("hello", str(123), "world")

print("나는 %d살입니다." % 20)
print("나는 %s살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
print("나는 {color1} 색과 {color2}새을 좋아해요." .format(color1 = "파란", color2 = "빨간"))

color1 = "파란"
color2 = "빨간"
print(f"나는 {color1}색과 {color2}색을 좋아해요.")

print("{0:,}" .format(1000000000) )


a = 123
b = "456"

print(str(a))
print(int(b))
print(float(b))
print(bool(a))



x = 13
y = 7
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

print(x & y)
print(x | y)
print(x ^ y)
print(x >> 3)
print(x << 3)

x = -2.5
print(x)
print(abs(x))

TT = [23123, 123,555,123]

for i in TT: print(i)


def printGooGoo():
    for i in range(1,10): 
        for j in range(1, 10):
            print(i*j, end=" ")
        print('')

printGooGoo()

def PrintPlus(x, y, z):
    a = x + y + z
    b = abs(x - y - z)
    c = x + y * z
    return a, b, c

print(PrintPlus(5, 4, 2))


def ChulSeng(year, month, date):
    print(year, "-", month, "-", date)

ChulSeng(1995, 6, 20)

a = 25
b = 23
c = 3

def MaxMinTT(a,b,c):
    a = 100
    return max(a, b, c), min(a, b, c)

print(a, b, c, "중 Max: %d, Min: %d" % MaxMinTT(a,b,c))


num = 10
def change_num():
    #global num
    num = 100
    print(num)

change_num()
print(num)


count = 10
for i in range(count):
    print("count = ", i)

start = 2
stop = 10
step = 3

for i in range(start, stop, step):
    print("count =", i)

a = 10
b = 5
if a > b:
    print(a)

for i in range(100):
    if i == 20:
        print("stop", i)
        break

for i in range(10):
    if i == 5:
        continue
    else:
        pass
    print(i)



count = 0
while (count < 10):
    print(count)
    count += 1

print("")


def PrintGooGooLine(x):
    TT = []
    for i in range(1, 10):
        TT.append(i * x)    
    return TT

for i in range(2, 10):
    print(PrintGooGooLine(i))