import random as rd

class Person:
    def __init__(self) -> None:
        self.name = "요곤요곤요"
        self.age = 432
        self.weight = 60
        self.health =  5

    def checkBadHealth(self):
        if self.health <= 0:
            print(f"건강해지려다 병이 나고 말았습니다 ㅠㅠ, 향년 {self.age}세")
            return True
        
        print("아직은 쌩쌩합니다!!")
        return False
    
    def run(self):
        self.weight -= 1
        self.health -= 1
        print(f"[체중: {self.weight}][건강상태: {self.health}] 뛰기: 달린다... 나는...")

    def golf(self):
        self.weight -= 2
        self.health -= 2
        print(f"[체중: {self.weight}][건강상태: {self.health}] 골프: 사장님 나이스샷~!")

    def swim(self):
        self.weight -= 2
        self.health -= 1
        print(f"[체중: {self.weight}][건강상태: {self.health}] 수영: 아냐짱, 어푸어푸!")

    def eat(self):
        self.weight += 2
        self.health += 1
        print(f"[체중: {self.weight}][건강상태: {self.health}] 먹기: 이 돼지 같은 놈!")

    def breaking(self):
        self.weight += 1
        self.health += 1
        print(f"[체중: {self.weight}][건강상태: {self.health}] 쉬기: 설마, 쉬는 거야?")

p1 = Person()

print(f"초기 측정\n이름: {p1.name}\n나이: {p1.age}세\n체중: {p1.weight}\n건강상태: {p1.health}\n\n")

year = 0
while True:
    year += 1
    if year > 5:
        year = 0
        p1.age += 1

    # a = input()
    if p1.checkBadHealth(): break

    a = rd.randint(1, 5)
    b = rd.randint(0, 40)
    if b == 0: 
        print(f"다 때려 칩니다. 현명합니다. [생존 나이: {p1.age}세]") 
        break

    if a == 1: p1.run()
    if a == 2: p1.golf()
    if a == 3: p1.swim()
    if a == 4: p1.eat()
    if a == 5: p1.breaking()