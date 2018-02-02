import sys
import math
sys.setrecursionlimit(1000000000)


def regularfalsi(ab, bb):
    x2 = ab - ((bb-ab)*(math.pow(ab, 4) - 32)/((math.pow(bb, 4) - 32)-(math.pow(ab, 4) - 32)))
    fx2 = math.pow(x2, 4) - 32
    if fx2 > 0:
            print("x0: ", ab, "\t\t\tx1: ", bb, "\t\t\tx2: ", x2)
            regularfalsi(ab, x2)
    elif fx2 < 0:
            print("x0: ", ab, "\t\t\tx1: ", bb, "\t\t\tx2: ", x2)
            regularfalsi(x2, bb)
    else:
        print("Root is: ", x2)


i = 2
j = 3
while (math.pow(i, 4) - 32) < 0:
    i += 1
while (math.pow(j, 4) - 32) > 0:
    j -= 1
x0 = i-1
x1 = j+1
regularfalsi(x0, x1)
