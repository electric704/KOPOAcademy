# 131
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)

# 132
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")

# 133
for 변수 in ["A", "B", "C"]:
  print(변수)

print("A")
print("B")
print("C")


# 134
for 변수 in ["A", "B", "C"]:
  print("출력:", 변수)

변수 = "A"
print("출력:", 변수)
변수 = "B"
print("출력:", 변수)
변수 = "C"
print("출력:", 변수)


# 135
for 변수 in ["A", "B", "C"]:
  b = 변수.lower()
  print("변환:", b)

변수 = "A"
b = 변수.lower()
print("변환:", b)
변수 = "B"
b = 변수.lower()
print("변환:", b)
변수 = "C"
b = 변수.lower()
print("변환:", b)

# 136
변수 = 10
print(변수)
변수 = 20
print(변수)
변수 = 30
print(변수)

리스트 = [10, 20, 30]
for 변수 in 리스트:
    print(변수)

# 137
for 변수 in [10, 20, 30]:
   print(변수)

# 138
for 변수 in [10, 20, 30]:
   print(변수)
   print("-------")

# 139
print("++++")
for 변수 in [10, 20, 30]:
   print(변수)

# 140
for i in range(4):
   print("-------")

# 141
리스트 = [100, 200, 300]
for i in 리스트:
   print(i + 10)

# 142
리스트 = ["김밥", "라면", "튀김"]
for i in 리스트:
   print("오늘의 메뉴: " + i)

# 143
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트:
   print(len(i))

# 144
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
   print(f"{i} +{len(i)}")

# 145
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
   print(i[0])

# 146
리스트 = [1, 2, 3]
for i in 리스트:
   print(f"3 X {i}")

# 147
리스트 = [1, 2, 3]
for i in 리스트:
   print(f"3 X {i} = {3 * i}")

# 148
리스트 = ["가", "나", "다", "라"]
for i in 리스트[1:]:
   print(i)

# 149
리스트 = ["가", "나", "다", "라"]
for i in 리스트[:2]:
   print(i)

# 150
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::-1]:
   print(i)


# 151
리스트 = [3, -20, -3, 44]
for i in 리스트:
   if i < 0:
      print(i)

# 152
리스트 = [3, 100, 23, 44]
for i in 리스트:
   if 0 == i % 3:
      print(i)

# 153
리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
   if 0 == i % 3 and i < 20:
      print(i)

# 154
리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
   if len(i) >= 3:
      print(i)

# 155
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
   if i.isupper():
      print(i)

# 156
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
   if i.islower():
      print(i)

# 157
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
   print(i.upper())

# 158
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for i in 리스트:
   print(i.split(".")[0])

# 159
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
   if "h" == i.split(".")[1]:
      print(i)

# 160
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
   if "h" == i.split(".")[1] or "c" == i.split(".")[1]:
      print(i)

# 161
for i in range(0, 100):
   print(i)

# 162
for i in range(2002, 2050, 4):
   print(i)

# 163
for i in range(3, 31,3):
   print(i)

# 164
for i in range(99):
   print(99-i)

for i in range(0, 100).__reversed__():
   print(i)

# 165
for i in range(0, 10):
   print(i * .1)

# 166
for i in range(3, 28, 3):
   print(f"3 X {int(i / 3)} = {i}")

# 167
for i in range(3, 28, 3):
   if 1 == int(i / 3) % 2:
       print(f"3 X {int(i / 3)} = {i}")

# 168
temp = 0
for i in range(1, 11):
   temp += i

print(temp)

# 169
temp = 0
for i in range(1, 11):
   if 1 == i % 2:
    temp += i

print(temp)

# 170
temp = 1
for i in range(1, 11):
   temp *= i

print(temp)

# 171
price_list = [32100, 32150, 32000, 32500]
for i in price_list:
   print(i)

# 172
price_list = [32100, 32150, 32000, 32500]
for i in price_list:
   print(price_list.index(i), i)

# 173
price_list = [32100, 32150, 32000, 32500]
for i in price_list:
   print(3 - price_list.index(i), i)

# 174
price_list = [32100, 32150, 32000, 32500]
for i in price_list[1:]:
   print(100 + ((price_list.index(i) - 1) * 10), i)

# callable -> 호출 가능한지 판별 (보통 함수는 호출 가능)
# 175
my_list = ["가", "나", "다", "라"]
for i in my_list[:-1]:
   print(f"{i} {my_list[my_list.index(i) + 1]}")

# 176
my_list = ["가", "나", "다", "라", "마"]
for i in my_list[:-2]:
    print(f"{i} {my_list[my_list.index(i) + 1]} {my_list[my_list.index(i) + 2]}")

# 177
my_list = ["가", "나", "다", "라"]
for i in my_list[2::-1]:
    print(f"{i} {my_list[my_list.index(i) - 1]}")

# 178
my_list = [100, 200, 400, 800]
for i in my_list[:-1]:
    print(f"{my_list[my_list.index(i) + 1] - i}")

# 179
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(0, len(my_list) - 2):
   print((my_list[i] + my_list[i+1] + my_list[i+2]) / 3)

# 180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []

for i in range(len(low_prices)):
   volatility.append(high_prices[i] - low_prices[i])

print(volatility)