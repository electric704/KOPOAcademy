from Module import tennis
from Module import soccer

import Module.golf as golf
## from Module import golf -- 동일

if __name__ == "__main__":
    pass

print(golf.g)
print(soccer.s)
print(tennis.t)

golf.func_g()
tennis.func_t()
soccer.func_s()

g = golf.c_g()
s = soccer.c_s()
t = tennis.c_t()

print(g.__call__())
print(t.__call__())
print(s.__call__())


def my_add(a, b): return a + b
def my_subtract(a, b): return a - b
def my_multiply(a, b): return a * b
def my_divide(a, b): return a / b


calc = [my_add, my_subtract, my_multiply, my_divide]

print(f"calc form: {type(calc)}")
print(calc)
print(f"A + B = {calc[0](5, 3)}")
print(f"A - B = {calc[1](5, 3)}")
print(f"A * B = {calc[2](5, 3)}")
print(f"A / B = {calc[3](5, 3)}")

calc = dict()

calc[0] = my_add
calc[1] = my_subtract
calc[2] = my_multiply
calc[3] = my_divide

print(f"calc form: {type(calc)}")
print(calc)
print(f"A + B = {calc[0](5, 3)}")
print(f"A - B = {calc[1](5, 3)}")
print(f"A * B = {calc[2](5, 3)}")
print(f"A / B = {calc[3](5, 3)}")


class MyAdd:
    def __call__(self, a, b): return a + b

class MySubtract:
    def __call__(self, a, b): return a - b

class MyMultiply:
    def __call__(self, a, b): return a * b

class MyDivide:
    def __call__(self, a, b): return a / b

calc = [MyAdd(), MySubtract(), MyMultiply(), MyDivide()]

print(f"calc form: {type(calc)}")
print(calc)
print(f"A + B = {calc[0](5, 3)}")
print(f"A - B = {calc[1](5, 3)}")
print(f"A * B = {calc[2](5, 3)}")
print(f"A / B = {calc[3](5, 3)}")

calc = dict()
calc[0] = MyAdd()
calc[1] = MySubtract()
calc[2] = MyMultiply()
calc[3] = MyDivide()


print(f"calc form: {type(calc)}")
print(calc)
print(f"A + B = {calc[0](5, 3)}")
print(f"A - B = {calc[1](5, 3)}")
print(f"A * B = {calc[2](5, 3)}")
print(f"A / B = {calc[3](5, 3)}")


data = [i for i in range(1, 100, 2)]
## data = {i:i for i in range(1, 100, 2)} -- dict
## data = {i for i in range(1, 100, 2)} -- set
## data = tuple(i for i in range(1, 100, 2)) -- tuple -> 그냥 하면 안됌
print(data)

data2 = list(map(lambda x: float(x+10), data))
print(data2)

import random as rd

lotto = [i for i in range(1, 46)]
rd.shuffle(lotto)

for i in range(0, 5): print(lotto[i])