import random
import cv2 as cv
import numpy as np


output = ""
f = open("engWord.txt", "rt", encoding='UTF8')
while True:
    c = f.read()
    if c == '':
        break
    output += c


f.close

print(output)
splitString = output.splitlines()
wordString = dict()
for i in splitString:
    aa = i.split(".")
    wordString[int(aa[0])] = [aa[1], aa[2], 0]

print(wordString)


while True:
    question = random.randint(1, len(wordString))
    print(wordString[question][0],"의 뜻은 무엇인가요?")
    ## 원래는 이거임
    ## a = input()

    answerRate = random.randint(0, 2)
    exitRate = random.randint(0, 100)
    input = question + answerRate
    a = ""
    if exitRate == 0:
        a = "0"
        print("종료")
    else:
        if input > len(wordString):
            continue
        a = wordString[input][1]
        print(a)

    ## 점수 설정
    if a == str(0):
        break
    elif a == wordString[question][1]:
        print(" O 맞았습니다!!")
        wordString[question][2] += 20
    else:
        print(" X 틀렸습니다!!")
        wordString[question][2] -= 10
        if wordString[question][2] < 0:
            wordString[question][2] = 0

while True:
    x = 40
    y = 1
    width = x * len(wordString) + 20
    height = 500
    depth = 3

    thickness = -1
    offset_x = 1
    offset_y = 10
    screen_start_x = 10
    screen_start_y = height - 50
    bgr = (0, 255, 0)

    img = np.zeros(shape = (height, width, depth)) # img = npzeros((height, width, depth), np.uint8)


    for i in wordString:
        
        for j in range(int(wordString[i][2])):
            
            start_x = screen_start_x + i * x
            start_y = screen_start_y - int(j * y / 2) * 5
            cv.rectangle(img, (start_x, start_y), (start_x + offset_x, start_y + offset_y), bgr, thickness)

        cv.putText(img, str(i), (int(i * x), screen_start_y + 20), cv.FONT_ITALIC, .5, (255,255,255), 0)
        cv.putText(img, wordString[i][0], (int(i * x) - 10, screen_start_y + 30), cv.FONT_ITALIC, .25, (255,255,255), 0)

    cv.imshow("test", img)
    cv.waitKey(0)