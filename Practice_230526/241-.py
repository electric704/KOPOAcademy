## 241
import datetime as dt

print(dt.datetime.now())

## 242
print(type(dt.datetime.now()))

## 243
for i in range(5, 0, -1):
    print(dt.datetime.now().date().day - i)

## 244
print(dt.datetime.now().strftime("%H:%M:%S"))

## 245
print(dt.datetime.strptime("2020-05-04", "%Y-%m-%d"))

## 246
import time

for i in range(0, 5):
    print(dt.datetime.now())
    time.sleep(1)

## 247 - 모듈을 임포트하는 4가지 방식에 대해 설명해보세요.

## 248
import os
print(os.getcwd())

## 249
#os.rename("C:/Users/hyunh/Desktop/before.txt", "C:/Users/hyunh/Desktop/after.txt")

## 250
import numpy as np
print(np.arange(.0, 5.0, .1))