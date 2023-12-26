import random as rd
import numpy as np
import cv2 as cv


mPlayerCount = 150
class Player:
    def __init__(self) -> None:
        self.coin = 10
        self.diceCount = 2
        self.score = 0
        self.nowScore = 0


playerList = list()
for i in range(mPlayerCount):
    playerList.append(Player())

def CheckGameisOver():
    for i in playerList:
        if i.score >= 1000:
            return False
        
    return True

## 점수값과 같은지 여부를 판별함
def ThrowDice(user):
    scoreList = list()
    for i in range(user.diceCount):
        scoreList.append(rd.randint(1, 6))

    sum = 0
    for i in scoreList:
        sum += i

    isSame = False
    isSameDict = {}
    for i in scoreList:
        try: isSameDict[i] += 1
        except: isSameDict[i] = 1

    
    if 1 == len(isSameDict):
        isSame =True
    else:
        isSame = False

    scoreList.clear()
    return sum, isSame

def SetGame(): 
    for i in playerList:
        ## 코인이 읎다.
        if not CheckCoin(i):
            continue

        ## 코인이 있당
        i.coin -= 1
        diceScore = 0
        result = ThrowDice(i)
        diceScore += result[0]

        ## 한 번만 더 한다.
        if result[1] == True:
            result = ThrowDice(i)
            diceScore += result[0]

        i.nowScore = diceScore

def CheckDiceScore():
    scoreList = list()

    for i in playerList:
        scoreList.append(i.nowScore)
    
    maxValue = max(scoreList)
    minValue = min(scoreList)

    for i in playerList:
        if i.nowScore == 0:
            continue
        elif i.nowScore == maxValue:
            i.nowScore *= 2
        elif i.nowScore == minValue:
            i.nowScore -= 30

    scoreList.clear()

def SetDiceScore():
    for i in playerList:
        i.score += i.nowScore

        if i.score < 0:
            i.score = 0
        i.nowScore = 0

def CheckCoin(user):
    if user.coin <= 0:
        user.coin = rd.randint(1, 10)
        return False
    
    return True


def PrintBox():
    x = 7
    y = 1
    width = x * mPlayerCount + 20
    height = 510
    depth =3

    thickness = -1
    offset_x = 5
    offset_y = 1
    screen_start_x = 10
    screen_start_y = height - 10
    bgr = (0, 255, 0)

    img = np.zeros(shape = (height, width, depth)) # img = npzeros((height, width, depth), np.uint8)

    for i in range(mPlayerCount):
        
        for j in range(playerList[i].score):
            
            start_x = screen_start_x + i * x
            start_y = screen_start_y - int(j * y / 2)
            cv.rectangle(img, (start_x, start_y), (start_x + offset_x, start_y + offset_y), bgr, thickness)

    cv.imshow("test", img)
    cv.waitKey(100)

def ResetGame():
    for i in playerList:
        i.coin = 10
        i.diceCount = 2
        i.score = 0
        i.nowScore = 0

while(True):
    if not CheckGameisOver():
        ResetGame()
    SetGame()
    CheckDiceScore()
    SetDiceScore()
    PrintBox()
