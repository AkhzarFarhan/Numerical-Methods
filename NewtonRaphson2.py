import math


def f(x):
    return math.exp(-x) - x


def fd(yi):
    return (-1)*math.exp(-yi) - yi


def nr(a):
    a.append(a[-1] - (f(a[-1])/fd(a[-1])))
    while True:
        if abs(a[-1] - a[-2]) > 0.00001:
            print("xi: ", a[-1])
            nr(a)
        else:
            break


aMain = [0, 0]
nr(aMain)
