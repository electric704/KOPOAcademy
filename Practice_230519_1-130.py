# 1
print("Hello World")

# 2
print("Mary\'s cosmetics")

# 3
print("신씨가 소리질렀다. \"도둑이야\"")

# 4
print("C:\\Windows")

# 5
print("안녕하세요.\n만나서\t\t반갑습니다.")

# 6
print("오늘은", "일요일")

# 7
print("naver", "kakao", "sk", "smasung", sep=";")

# 8
print("naver", "kakao", "sk", "smasung", sep="/")

# 9
print("first", end="");print("second")

# 10
print("5/3 = ", 5/3)

# 11
삼성전자 = 50000
삼성전자주식 = 삼성전자 * 10
print("총 평가금액: ", 삼성전자주식)

# 12
시가총액 = 298,000,000,000,000
현재가 = 50,000
PER = 15.79

print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

# 13
s = "hello"
t = "python"

print(s + "! " + t)

# 14
print(2 + 2 * 3)

# 15
a = 128
print(type(a))

# 16
num = "720"
print(num, type(num))

num = int(num)
print(num, type(num))

# 17
num_str = 100
print(num_str, type(num_str))

num_str = str(num_str)
print(num_str, type(num_str))

# 18
fnum = float("15.79")

# 19
year = "2020"
year = int(year)
print(year - 3)
print(year - 2)
print(year - 1)

# 20
월가격세금 = 48584
무이자개월 = 36
print("총 금액: ", 월가격세금 * 무이자개월)

# 쪽지
print(s, t, year + 3, sep = " ")

# 21
letters = 'python'
print(letters[0], letters[2])

# 22
license_plate = "24가 2210"
print(license_plate[-4:])

# 23
string = "홀짝홀짝홀짝"
print(string[::2])

# 24
string = "PYTHON"
print(string[::-1])

# 25
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

# 26
print(phone_number.replace("-", ""))

# 27
url = "http://sharebook.kr"
print(url.split('.')[1])

# 28
lang = 'python'
# lang[0] = 'P'
print(lang)

# 29
string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'))

# 30
string = 'abcd'
print(string.replace('b', 'B'))

# 31
a = "3"
b = "4"
print(a + b)

# 32
print("Hi" * 3)

# 33
print("-" * 80)

# 34
t1 = 'python'
t2 = 'java'
print((t1 + " " + t2 + " ") * 4)

# 35
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# 36
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

# 37
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

# 38
상장주식수 = "5,969782,550"
print(int(상장주식수.replace(",","")))

# 39
분기 = "2020/03(E) (IFRS연결)"
print(분기.split("(")[0])

# 40
data = "   삼성전자    "
print(data.replace(" ", ""))

# 41
ticker = "btc_krw"
print(ticker.upper())

# 42
ticker = "BTC_KRW"
print(ticker.lower())

# 43
print("hello world!".capitalize())

# 44
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

# 45
file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx", "xls")))

# 46
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

# 47
a = "hello world"
print(a.split(" "))

# 48
ticker = "btc_krw"
print(ticker.split("_"))

# 49
date = "2020-05-01"
date = date.split("-")
print(date[0] + "년" + date[1] + "월" + date[2] + "일")

# 50
data = "039490     "
print(data.rstrip())

# 51
movie_rank  = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

# 52
movie_rank.append("배트맨")
print(movie_rank)

# 53
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 54
movie_rank.remove("럭키")
print(movie_rank)

# 55
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# 56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1 + lang2
print(langs)

# 57
nums = [1, 2, 3, 4, 5, 6, 7]
print(f"max: {max(nums)}, min: {min(nums)}")

# 58
nums = [1, 2, 3, 4, 5]
print(f"sum: {sum(nums)}")

# 59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(f"count: {cook.count}")

# 60
nums = [1, 2, 3, 4, 5]
print(f"avg: {sum(nums) / len(nums)}")

# 61
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(f"가격: {price[1:]}")

# 62
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"홀수: {nums[::2]}")

# 63
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"짝수: {nums[1::2]}")

# 64
nums = [1, 2, 3, 4, 5]
print(f"역방향: {nums[::-1]}")

# 65
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# 66
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

# 67
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

# 68
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

# 69
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

# 70
data = [2, 4, 3, 1, 5, 10, 9]
data.sort(reverse=True)
print(data)

# 71
my_variable = ()
print(type(my_variable))

# 72
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank, type(movie_rank))

# 73
tupleset = (1, )
print(tupleset, type(tupleset))

# 75
t = 1, 2, 3, 4
print(type(t))

# 76
t = ('a', 'b', 'c')
print(t)
t = ('A', 'b', 'c')
print(t)

# 77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(interest, type(interest))

interest = list(interest)
print(interest, type(interest))

# 78
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(interest, type(interest))

interest = tuple(interest)
print(interest, type(interest))

# 79
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# 80
temp = tuple(range(2, 100, 2))
print(temp)

# 81
a, b, *c = (0, 1, 2, 3, 4, 5)
print(a, b, c)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores
print(a, b, valid_score)

# 82
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores
print(a, b, valid_score)

# 83
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score, b = scores
print(a, b, valid_score)

# 84
temp = {}
print(temp, type(temp))

# 85
icecream = { '메로나' : 1000, '폴라포' : 1200, '빵바레' : 1800 }
print(icecream, type(icecream))

# 86
icecream.update({'죠스바' : 1200, '월드콘' : 1500})
print(icecream, type(icecream))

# 87
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print(f"메로나 가격: {ice['메로나']}")

# 88
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice["메로나"] = 1300
print(ice)

# 89
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice.pop('메로나')
print(ice)

# 91
inventory = { "메로나" : [300, 20], "비비빅" : [400, 3], "죠스바" : [250, 100]}
print(inventory)

# 92
inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
print("%d원" % inventory["메로나"][0])

# 93
inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
print("%d개" % inventory["메로나"][1])

# 94
inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}

# 95
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = icecream.keys()
print(ice)

# 96
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = icecream.values()
print(ice)

# 97
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(sum(icecream.values()))

# 98
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

# 99
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

# 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
print(dict(zip(date, close_price)))

# 102
print(3 == 5)

# 103
print(3 < 5)

# 104
x = 4
print(1 < x < 5)

# 105
print ((3 == 3) and (4 != 3))

# 106
# print(3 => 4)
print(3 <= 4)

# 107
if 4 < 3:
    print("Hello World")

# 108
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")

# 109
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")

# 110
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")

# 111
a = input("입력: ")
print(a * 2)

# 112
num = int(input("숫자를 입력하세요: "))
print(num + 10)

# 113
num = int(input("숫자를 입력하세요: "))
if 0 == (num % 2):
    print("해당 숫자는 짝수입니다.")
else:
    print("해당 숫자는 홀수입니다.")

# 114
a = int(input("숫자를 입력하세요: ")) + 20
if a > 255:
    print(255)
else:
    print(a)

# 115
a = int(input("숫자를 입력하세요: ")) - 20
if a > 255:
    print(255)
elif a < 0:
    print(0)
else:
    print(a)

# 116
x = input("현재시간: ").split(":")

if len(x) == 2:
    if x[1] == "00":
        print("정각입니다.")
    else:
        print("정각이 아닙니다.")

# 117
fruit = ["사과", "포도", "홍시"]
a = input("과일 이름을 입력하세요.")
if a in fruit:
    print(f"{a}는 과일입니다!")
else:
    print("과일이 아닙니다...")

# 118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

if input("투자 종목은?") in warn_investment_list:
    print("투자 경고 종목입니다!!")
else:
    print("투자 경고 종목이 아닙니다.")

# 119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
if input("제가 좋아하는 계절은?") in list(fruit.keys()):
    print("정답입니다!")
else:
    print("정답이 아닙니다.")

# 120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
if input("제가 좋아하는 계절과일은?") in list(fruit.values()):
    print("정답입니다!")
else:
    print("정답이 아닙니다.")

# 121
a = input("문자 하나 입력: ")
if a.isupper():
    print(a.lower())

else:
    print(a.upper())

# 122
score = int(input("학점: "))
grade = ""
if score >= 81 and score <= 100:
    grade = "A"

elif score >= 61 and score <= 80:
    grade = "B"

elif score >= 41 and score <= 60:
    grade = "C"

elif score >= 21 and score <= 40:
    grade = "D"

elif score >= 0 and score <= 20:
    grade = "F"

print("grade is " + grade)

# 123
hwanyul = { "달러" : 1167, "엔" : 1.096, "유로" : 1268, "위안" : 171 }
tt = input("원(Won)으로 계산 금액은? (ex: xx 달러)").split()
# tt, aa = input("원(Won)으로 계산 금액은? (ex: xx 달러)").split()

if len(tt) == 2:
    print(f"{hwanyul[tt[1]] * int(tt[0])}입니다.")


# 124
a = int(input("첫 번째 숫자: "))
b = int(input("두 번째 숫자: "))
c = int(input("세 번째 숫자: "))

print(f"가장 큰 숫자는 {max((a, b, c))}입니다.")

# 125
telecom = { "011" : "SKT", "016" : "KT", "019" : "LGU", "010" : "알수없음"}
a, b, c = input("휴대전화 번호 입력: ex) xxx-xxxx-xxxx").split("-")

if a in telecom:
    print(f"당신은 {telecom[a]} 사용자 입니다.")

# 126
postNum = { 0 : "강북구", 1: "강북구", 2: "강북구", 3: "도봉구", 4: "도봉구", 5: "도봉구", 6:"노원구", 7:"노원구", 8:"노원구", 9:"노원구"}
a = input("우편번호: ")
if len(a) >= 3:
    print(postNum[int(a[2])])


# 127
a, b = input("주민등록번호: ex)xxxxxxx-xxxxxxxx").split("-")
if b[0] == "1" or b[0] == "3":
    print("당신은 남자입니다.")
elif b[0] == "2" or b[0] == "4":
    print("당신은 여자입니다.")

# 128
a, b = input("주민등록번호: ex)xxxxxxx-xxxxxxxx").split("-")
if 0 <= int(b[1:2]) <= 8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")


# 129
a = input("주민등록번호: ex)xxxxxxx-xxxxxxxx")
a = a.replace("-", "")
if len(a) >= 13:
    if int(a[-1]) == 11 - ((int(a[0]) * 2 + int(a[1]) * 3 + int(a[2]) * 4 + int(a[3]) * 5 + int(a[4]) * 6
                             + int(a[5]) * 7 + int(a[6]) * 8 + int(a[7]) * 9 + int(a[8]) * 2 + int(a[9]) * 3 + int(a[10]) * 4 + int(a[11]) * 5) % 11):
        print("유효한 주민등록번호입니다.")
    else:
        print("유효하지 않은 주민등록번호입니다.")

# 130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
if int(btc["opening_price"]) < int(btc["max_price"]) - int(btc["min_price"]):
    print("상승장입니다.")
else:
    print("하락장입니다.")