def sum(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def sub(a, b):
    return a / b



print(sum(5, 3))
print(minus(5, 3))
print(multi(5, 3))
print(sub(5, 3))



## Filter -> 함수를 통과한 값들만 추려서 배열화
def func1(n):
    return n < 3

ls = [1, 2, 3, 4, 5]
ls2 = filter(func1, ls)

print(list(ls2))


## Reduce 각 요소를 연산한 뒤 이전 연산 결과들과 누적해서 반환
from functools import reduce

num = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, num)

print(f"total = {total}")


#Z Zip zip -> 하나씩 묶어서 튜플로, map -> 묶어서 리스트로 filter와 차이라면 함수가 들어가지 않음

a = ['a', 'b', 'c', 'd']
b = [1, 2, 3, 4]
c = ['A', 'B', 'C']

s = list(zip(a, b, c))
print(s)

ss = list(map(list, s))
print(ss)


# iterable -> 반복할 수 있는 애이지만 반복하는 애는 아님,  iterator -> 본격적으로 반복하는 애
# 부가설명
# Iterable은 List처럼 데이터를 순회할 수 있는 객체입니다.
# Iterator는 Iterable 객체를 순회하는 객체입니다.
# Iterable은 iter() 메소들로 Iterator 객체를 생성할 수 있습니다.
# Iterator는 __next__() 메소드로 Iterable의 데이터에 순차적으로 접근할 수 있습니다.
# Iterator 객체는 항상 Iterable 객체가 됩니다. 하지만 Iterable 객체는 Iterator 객체가 될 수 있지만 아닐 수도 있습니다.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = iter(lst)

print(next(i))
print(next(i))
print(next(i))


print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i)

for s in i:
    print(s)


# 제귀함수
def recur(count):
    if count == 0:
        return
    print(count)
    count -= 1
    recur(count)

recur(5)
          

# 파일 읽기 쓰기
# f = open('test.txt', 'w')
# f.write('Python write')
# f.close()

f = open('test.txt', 'r')
# s1 = f.read()
# # s1 = f.read(5)
# print(s1)

s2 = f.readline()
print(s2)

# s3 = f.readlines()
# print(s3)
# print(s3[1])
f.close()



# 1부터 100까지 텍스트파일에 Write 해보기
f = open('Number.txt', 'w')

for i in range(1, 101):
    f.write(f'{i}'+'\n')

f.close()


f = open('Number.txt', 'r')

ls = f.readlines()
print(list(map(int, ls)))

f.close()


# json -> 파이썬은 json 데이터를 딕셔너리로 받아온다.
import json

s1 = dict()
s1['a1'] = 'apple'
s1['a2'] = 'banana'

s2 = dict()
s2['a1'] = 'gold'
s2['a2'] = 'silver'

s3 = dict()
s3['s1'] = s1
s3['s2'] = s2
print(s3)

with open('test.json', 'w', encoding='utf-8') as s:
    json.dump(s3, s, indent=4)


with open('test.json', 'r') as jf:
    #json_data = f.read()       # <-- str
    #json_data = f.readline()   # <-- str
    #json_data = f.readlines()  # <-- list
    json_data = json.load(jf)   # <-- dict(가장 편한방법)

print(json.dumps(json_data))

# dumps -> s 시에는 string으로 변환이 된다.

print(type(json_data))
print(type(json.dumps(json_data)))
print(json_data)
print(json.dumps(json_data)[5])


# 2차원 리스트
data = [[10, 15],
        [20, 25],
        [30, 35]]

print(data[1][1])

data[2][0] = 50
print(data[2][0])


# 톱니형 리스트
data = [[10, 15],
        [20, 25, 10, 8, 55, 1],
        [3],
        [14, 7, 40, 0]]


print(data[1][1])
data[2][0] = 50
print(data[1][4])


# append 이차원 리스트
data = []
data.append([])
data[0].append(10)
data[0].append(10)
data.append([])
data[1].append(1)
data[1].append(2)
data[1].append(3)

print(data)


# list와 tuple 에러 -> tuple은 const 속성일 못바꿈
data1 = ((0,1), (2,3), (4,5))
data2 = ([0,1], [2,3], [4,5])
data3 = [(0,1), (2,3), (4,5)]

# data1[1][1] = 10
# data1[1] = (10, 10)

data2[1][1] = 10
# data2[1] = (10, 10)

# data3[1][1] = 10
data3[1] = (10, 10)


# 파이썬 만의 편리한 2차원 3차원 초기화
data1 = [[0 for i in range(3)] for j in range(5)]
data2 = [[[0 for i in range(3)] for j in range(5)]for k in range(10)]

print(data1)
print(data2)


# 함수 내 함수
def c_func():
    a= 5
    b = 2
    def calc(x):
        return x * a + b
    return calc

cf = c_func()

print(cf(3), cf(10))


# try
try:
    data1 = list(range(3))
    print(data1[2])
    print(data1[2])

except:
    print("except")
    print(data1[2])

else:
    print("else")

finally:
    print("finally")



    

# dictionary 값이랑 키 가져오는 행위

data = dict()
data['a1'] = 'apple'
data['a2'] = 'banana'
data['a3'] = 'gold'
data['a4'] = 'silver'

for key in data:
    print(key)

for key in data.keys():
    print(key)

for value in data.values():
    print(value)

for key, value in data.items():
    print(f'{key}, {value}')
