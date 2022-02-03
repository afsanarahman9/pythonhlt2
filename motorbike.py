
import random


def function1(c):
    f = 10/1000 * c
    c = c-f
    return c


c = 2000
while c > 1000:
    c = function1(c)

print(c)
