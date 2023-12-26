import random
from math import *

bizidoSize = 2000
bizidoList = list(range(bizidoSize))

gunzipCount = 5
gunzipInitPointList = list(range(gunzipCount))

for i in range(len(bizidoList)):
    bizidoList[i] = [random.randrange(0, 100), random.randrange(0, 100)]

for i in range(len(gunzipInitPointList)):
    gunzipInitPointList[i] = [random.randrange(0, 100), random.randrange(0, 100)]

# 점과 점사이 거리계산 - 유클리드 계산
def PointDistance(P1, P2):
    return(sqrt((P2[0] - P1[0]) ** 2 + (P2[1] - P1[1]) ** 2))

# 군집중심들의 거리와 데이터 간의 거리 비교 후 최소거리 반환
# 최소거리를 가진 순서를 반환하여 인덱스 설정
def GunzipToIndex(distancelist):
    return distancelist.index(min(distancelist))

# 대충 잡고 보장
gunzipPointList = list(range(gunzipCount))
gunzipAvgPointList = list(range(gunzipCount))

# 2차원 좌표
for i in range(len(gunzipPointList)):
    gunzipPointList[i] = [range(2)]

# 군집된거 가까운 데로 정리
def JungLee():
    for i in range(gunzipCount):
        gunzipPointList[i].clear()

    for i in range(len(bizidoList)):

        distanceList = []
        
        for j in range(gunzipCount):
            distanceList.append(PointDistance(bizidoList[i], gunzipInitPointList[j]))

        Index = GunzipToIndex(distanceList)
        gunzipPointList[Index].append(bizidoList[i])
        distanceList.clear()


# 지금 나온 평균과 이전에 나온 평균 비교해서 같으면 참값 반환(더이상 학습할 필요 업슴)
def CheckAvgVsPrev():
    for i in range(len(gunzipAvgPointList)):
        if(gunzipInitPointList[i] == gunzipAvgPointList[i]):
            continue
        else:
            for i in range(len(gunzipAvgPointList)):
                gunzipAvgPointList[i] = gunzipInitPointList[i]

            return False
        
    return True

def gunzipReset():
    for i in range(len(gunzipInitPointList)):
        gunzipInitPointList[i] = PyungGyun(i, gunzipPointList)


# 군집된 거 평균
def PyungGyun(index, list):

    sumX = 0
    sumY = 0

    for i in range(len(list[index])):
        sumX += list[index][i][0]
        sumY += list[index][i][1]

    if(len(list[index]) != 0):
        return [(sumX / len(list[index])), (sumY / len(list[index]))]
    else:
        return [0, 0]


# 본격 코어 코드
while not CheckAvgVsPrev():
    JungLee()
    gunzipReset()
    print(gunzipAvgPointList)


# 화면 출력
import matplotlib.pyplot as plt
plt.figure(figsize=(7, 7))

for i in range(gunzipCount):
    X = [j[0] for j in gunzipPointList[i]]
    Y = [j[1] for j in gunzipPointList[i]]
    plt.scatter(X, Y, s=60, alpha=0.5)

x = [i[0] for i in gunzipAvgPointList]
y = [i[1] for i in gunzipAvgPointList]
plt.scatter(x, y, s=100, alpha=1)
plt.show()