## 181
apart = [["101호", "102호"], ["201호", "202호"], ["301호", "303호"]]
print(apart, type(apart))

## 182
stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]
print(stock, type(stock))

## 183
stock = {"시가": [100, 200, 300], "종가":[80, 210, 330]}
print(stock, type(stock))

## 184
stock = {"10/10": [80, 110,70, 90], "10/11":[210,230,190,200]}
print(stock, type(stock))

## 185
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(str(j) + " 호")

## 186
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for j in i:
        print(str(j) + " 호")

## 187
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for j in i[::-1]:
        print(str(j) + " 호")

## 188
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(str(j) + " 호")
        print("-----")

## 189
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(str(j) + " 호")
    print("-----")

## 190
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(str(j) + " 호")

print("-----")


## 191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
susu = 100.014 * .01
for i in data:
    for j in i:
        print((j * susu))

## 192
for i in data:
    for j in i:
        print((j * susu))
    print("-" * 4)

## 193
result = []
for i in data:
    for j in i:
        result.append(j * susu)

print(result)


## 194
result = []
for i in data:
    temp = []
    for j in i:
        temp.append(j * susu)
    result.append(temp)

print(result)


## 195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:]:
    for j in i[3:]:
        print(j)


## 196
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:]:
    for j in i[3:]:
        if j > 150:
            print(j)

## 197
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:]:
    for j in i[3:]:
        if j >= i[0]:
            print(j)


## 198
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

volatility = []
for i in ohlc[1:]:
    volatility.append(i[1] - i[2])

print(volatility)


## 199
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:]:
    for j in i[3:]:
        if j > i[0]:
            print(i[1] - i[2])


## 200
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

volatility = []
sumnum = 0
for i in ohlc[1:]:
    volatility.append(i[3] - i[0])

for i in volatility:
    sumnum += i

print(sumnum)

## 201
def print_coin():
    print("비트코인")

## 202
print_coin()

## 203
for i in range(100):
    print_coin()

## 204
def print_coins():
    for i in range(100):
        print_coin()

## 205
## hello()
def hello():
    print("Hi")

## 206 - 예측
def message() :
    print("A")
    print("B")

message()
print("C")
message()

## 207 - 예측
print("A")

def message() :
    print("B")

print("C")
message()

## 208 - 예측
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()

## 209 - 예측
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

## 210 - 예측
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()

## 211 - 예측
def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")

## 212 - 예측
def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8)

## 213 - 에러 원인
def 함수(문자열) :
    print(문자열)

# 함수()

## 214 - 에러 원인
def 함수(a, b) :
    print(a + b)

# 함수("안녕", 3)

## 215
def print_with_smile(문자열) :
    print(문자열 + ":D")

## 216
print_with_smile("안녕하세요")

## 217
def print_upper_price(현재가격):
    print(현재가격 * 1.3)

## 218
def print_sum(a, b):
    print(a + b)

## 219
def print_arithmetic_operation(a,b):
    print (f"{a} + {b} = {a + b}")
    print (f"{a} - {b} = {a - b}")
    print (f"{a} * {b} = {a * b}")
    print (f"{a} / {b} = {a / b}")

## 220
def print_max(a, b, c):
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)

## 221
def print_reverse(문자열):
    print(문자열[::-1])

## 222
def print_score(score_list):
    print(sum(score_list) / len(score_list))
print_score([1, 2, 3])

## 223
def print_even(num_list):
    for i in num_list:
        if i % 2 == 0 :
            print(i)

print_even([1, 3, 2, 10, 12, 11, 15])

## 224
def print_keys(dict_sample):
    for i in dict_sample.keys():
        print(str(i))    

print_keys ({"이름":"김말똥", "나이":30, "성별":0})

## 225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(mydict, mydict_key):
    print(mydict[mydict_key])

print_value_by_key  (my_dict, "10/26")

## 226
def print_5xn(string):
    for i in range(int(len(string) / 5)):
        print(string[i * 5: i * 5 + 5])

print_5xn("아이엠어보이유알어걸")

## 227
def print_mxn(string, m):
    for i in range(int(len(string) / m)):
        print(string[i * m: i * m + m])

print_mxn("아이엠어보이유알어걸", 3)

## 228
def calc_monthly_salary(annual_salary):
    print(annual_salary / 12)

## 229 - 예측
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)

## 230 - 예측
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)

## 231 - 예측
def n_plus_1 (n) :
    result = n + 1

n_plus_1(3)
print (result)

## 232
def make_url(site_string):
    print("www." + site_string + ".com")

## 233
def make_list(string_letter):
    temp = []
    for i in string_letter:
        temp.append(i)

    return temp
print(make_list("abcd"))

## 234
def pickup_even(num_list):
    temp = []
    for i in num_list:
        if i % 2 == 0:
            temp.append(i)
    
    return temp

print(pickup_even([3, 4, 5, 6, 7, 8]))

## 235
def convert_int(sample_string):
    return int(sample_string.replace(",", ""))

print(convert_int("1,234,567"))

## 236 - 예측
def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

## 237 - 예측
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)


## 238 - 예측
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

## 239 - 예측
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)

## 240 - 예측
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)