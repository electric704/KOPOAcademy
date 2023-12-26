import random as rd

class Car:
    def __init__(self) -> None:
        self.dist = 0
        self.fuel = 100
        print("부릉부릉~!")

    def act(self):
        a = rd.randint(0, 4)
        if      a == 0: self.go()
        elif    a == 1: self.stop()
        elif    a == 2: self.left()
        elif    a == 3: self.right()
        elif    a == 4: self.uturn()

    def go(self):
        self.fuel -= 15
        self.dist += 3
        print("드가자!!")

    def stop(self):
        self.fuel -= 5
        self.dist += 1
        print("이건 좀...;;")

    def left(self):
        self.fuel -= 10
        self.dist += 2
        print("왼")

    def right(self):
        self.fuel -= 10
        self.dist += 2
        print("우")

    def uturn(self):
        self.fuel -= 10
        self.dist += 2
        print("풀백!!!")

    def checkFuel(self):
        return (self.fuel <= 0)
        

mekaCar = Car()

while True:
    if mekaCar.checkFuel():
        print("못달리뮤ㅠ")
        print(f"남은 연료: {mekaCar.fuel}")
        print(f"달린 거리: {mekaCar.dist}")
        break
    
    mekaCar.act()