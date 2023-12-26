mEndCondition = 10
mGameCount = 0
mPlayersNumber = 3
mPlayerList = list()
mGameTool = { 1 : "Rock", 2 : "Sissor", 3 : "Paper"}

import random

class Person:
    def __init__(self) -> None:
        self.hand = 1
        self.winsCount = 0
        self.loseCount = 0
        self.drawCount = 0

for i in range(mPlayersNumber):
    mPlayerList.append(Person())

def CheckEndGame():
    for i in mPlayerList:
        if i.winsCount >= mEndCondition:
            return True
    
    return False

def UpdateHand():
    for i in mPlayerList:
        i.hand = random.randint(1, 3)

def CheckHands(toolName):
    sum = 0
    for i in mPlayerList:
        if mGameTool[i.hand] == toolName:
            sum += 1

    return sum

def SetDrawCount():
    for i in mPlayerList:
        i.drawCount += 1

def SetWinCount(hand):
    for i in mPlayerList:
        if mGameTool[i.hand] == hand:
            i.winsCount += 1

def SetLoseCount(hand):
    for i in mPlayerList:
        if mGameTool[i.hand] == hand:
            i.loseCount += 1

def UpdateResult():
    rockCount = CheckHands("Rock")
    sissorCount = CheckHands("Sissor")
    paperCount = CheckHands("Paper")

    if rockCount == mPlayersNumber or sissorCount == mPlayersNumber or paperCount == mPlayersNumber:
        SetDrawCount()
    
    elif rockCount == 0:
        SetWinCount("Sissor")
        SetLoseCount("Paper")

    elif sissorCount == 0:
        SetWinCount("Paper")
        SetLoseCount("Rock")

    elif paperCount == 0:
        SetWinCount("Rock")
        SetLoseCount("Sissor")

    else:
        SetDrawCount()

def UpdateDebug():
    for i in mPlayerList:
        print(mGameTool[i.hand], end= " ")
        print(i.winsCount, end= " ")
        
    print("------------")

while(not CheckEndGame()):
    UpdateHand()
    UpdateResult()
    UpdateDebug()
    mGameCount += 1

for i in mPlayerList:
    if i.winsCount >= mEndCondition:
        print(f"우승자는 [플레이어 {mPlayerList.index(i) + 1}] 입니다!!!")
        print(f"총 경기수: {mGameCount}\t승: {i.winsCount}\t무: {i.drawCount}\t패: {i.loseCount}")
        print(f"승률: {round(i.winsCount / mGameCount * 100)}%")