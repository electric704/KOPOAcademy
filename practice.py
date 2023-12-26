# 애완동물을 소개해 주세요
Animal = '고양이'
Name = '뭉밍이'
Hobby = '낮잠'
Age = 4
isAdult = Age >= 3

'''
오오아오오왕
'''

print("우리집 " + Animal + "의 이름은 " + Name + "에요")
Hobby = '공놀이'
print(Name + "은(는) " + str(Age) + "살이며, " + Hobby +"을(를) 아주 좋아해요")
print(Name + "은(는) 어른일까요? " + str(isAdult))

station = '사당'
print(station + '행 열차가 들어오고 있습니다.')
station = '신도림'
print(station + '행 열차가 들어오고 있습니다.')
station = '인천공항'
print(station + '행 열차가 들어오고 있습니다.')

print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3)
print(5%3)
print(10%3)
print(5//3)
print(10//3)

print(10>3)
print(4>=7)
print(10<3)
print(5<=5)

print(3==3)
print(1!=3)
print(not 1!=3)

print((3>0) and (3<5))
print((3>0) or (3<5))
print(2+3*4)
print((2+3)*4)

number = 2 + 3* 4
print(number)
number = number + 2
print(number)
number+=2
print(number)
number/=2
print(number)
number-=2
print(number)

print(abs(-4))
print(pow(4,2))
print(max(5,12))
print(min(5,12))
print(round(3.14))
print(round(5.99))

from math import *
# module -> package -> library
# header -> namespace -> library
# *은 모든 걸 다 가져온다

# from math import => 수학 라이브러리 가져옴
print(floor(4.99))  # 버림
print(ceil(3.14))   # 올림
print(sqrt(2))

from random import *
print(random())
print(random() * 10)
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10 + 1))
# print(int(random() * 10 + 1))
# print(int(random() * 10 + 1))
# print(int(random() * 10 + 1))
# print(int(random() * 10 + 1))
# print(int(random() * 10 + 1))

# print(int(random() * 45 + 1))
# print(randrange(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))

date = randint(4,28)
print('오프라인 스터디 모임 날자는 매월 ' + str(date) + "일로 선정되었습니다.")

sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요."
print(sentence2)
sentence3 = """
나는 소년입니다.
파이썬은 쉬워요.
"""
print(sentence3)

jumin = "990120-1234567"
print("성별: " + jumin[7])
print("연: " + jumin[0:2])
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])

print("생년월일: " + jumin[:6])
print("뒤 7자리: " + jumin[7:])
print("뒤 7자리: " + jumin[-7:])

python = 'Python is Amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace('Python', 'Java'))

index = python.index('h')
print(index)
index = python.index('n', index+1)
print(index)

print(python.find("n"))
print(python.find("Java"))

print(python.count('n'))

print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이선")
print("Apple %c로 시작해요." % "A")

print("나는 {}살입니다.". format(20))
print("나는 {age}살이며, {color}색을 좋아해요.". format(age = 20, color = "빨강"))

print("백문이 불여일견\n백견이 불여일타")
print("저는 \"나도코딩\"입니다.")
print("C:\\Users\\DELL\\Desktop\\pythonworkspace")

print("Red Apple\rPine")
print("Redd\bApple")
print("Red\tApple")

url = "http://github.com"
myStr = url.replace("http://", "")
print(myStr)
myStr = myStr[:myStr.index(".")]
print(myStr)

myStr = myStr[:3] + str(len(myStr)) + str(myStr.count('e')) + "!"
print(myStr)


subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1, "정형돈")
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

subway.append("유재석")
print(subway.count("유재석"))

numList = [5,2,4,3,1]
numList.sort()
print(numList)

numList.reverse()
print(numList)

numList.clear()
print(numList)

mixList = ["조세호", 20, True]
print(mixList)

numList.extend(mixList)
print(mixList)