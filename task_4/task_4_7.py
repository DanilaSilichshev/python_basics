from itertools import count
from math import factorial

n = int(input("Введите число: "))


def fact():
    for element in count(1):
        yield factorial(element)


i = 0
for num in fact():
    if i < n:
        print(num)
        i += 1
    else:
        break
