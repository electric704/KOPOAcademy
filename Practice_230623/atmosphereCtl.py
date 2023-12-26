import random as rd
import time

class Atmo:
    def __init__(self) -> None:
        self.temper = rd.randint(0, 30)
        self.water = rd.randint(0, 100)

    def resetTemper(self):
        self.temper = rd.randint(0, 30)
        print(f"온도가 재설정 됩니다. [온도: {self.temper}][습도: {self.water}]")
    
    def resetWater(self):
        self.water = rd.randint(0, 100)
        print(f"습도가 재설정 됩니다. [온도: {self.temper}][습도: {self.water}]")

    def coolingTemper(self):
        self.temper -= 1

    def removingWater(self):
        self.water -= 1

class Product:
    def __init__(self) -> None:
        self.awayTime = 0
        self.isActing = False

    def turnOn(self):
        self.isActing = True

    def turnOff(self):
        self.isActing = False

    def acting(self):
        self.awayTime = 0

    def away(self):
        self.awayTime += 1

    def isLimitAway(self):
        return self.awayTime > 5


class Aircon(Product):
    def acting(self):
        super().acting()

    def turnOn(self):
        print(f"----- 에어컨 가동시작 -----")
        super().turnOn()

    def turnOff(self):
        print(f"----- 에어컨 가동중지 -----")
        super().turnOff()

class dehumidi(Product):
    def acting(self):
        super().acting()

    def turnOn(self):
        print(f"----- 제습기 가동시작 -----")
        super().turnOn()

    def turnOff(self):
        print(f"----- 제습기 가동중지 -----")
        super().turnOff()


air = Atmo()
ac = Aircon()
dh = dehumidi()

while True:
    if not ac.isActing:
        ac.away()
        print(f"[온도: {air.temper}][습도: {air.water}] 에어컨 Off")
        if ac.isLimitAway():
            air.resetTemper()
    elif ac.isActing:
        print(f"[온도: {air.temper}][습도: {air.water}] 에어컨 On")
        ac.acting()
        air.coolingTemper()

    if not dh.isActing:
        dh.away()
        print(f"[온도: {air.temper}][습도: {air.water}] 제습기 Off")
        if dh.isLimitAway():
            air.resetWater()
    elif dh.isActing:
        print(f"[온도: {air.temper}][습도: {air.water}] 제습기 On")
        dh.acting()
        air.removingWater()

    if air.temper > 25 and not ac.isActing:
        ac.turnOn()
    elif air.temper < 20 and ac.isActing:
        ac.turnOff()    
    if air.water > 60 and not dh.isActing:
        dh.turnOn()
    elif air.water < 40 and dh.isActing:
        dh.turnOff()

    # time.sleep(1)
    time.sleep(0.25)