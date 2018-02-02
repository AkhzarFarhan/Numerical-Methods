import sys
import math
sys.setrecursionlimit(1000000000)


def regularfalsi(ab, bb):
    if abs(ab-bb) > 0.00001:
        x2 = ab - ((bb-ab)*(math.cos(ab) - ab*math.exp(ab))/((math.cos(bb) - bb*math.exp(bb))-(math.cos(ab) - ab*math.exp(ab))))
        fx2 = math.cos(x2) - x2*math.exp(x2)
        if fx2 > 0:
                print("x0: ", ab, "\t\t\tx1: ", bb, "\t\t\tx2: ", x2)
                regularfalsi(ab, x2)
        elif fx2 < 0:
                print("x0: ", ab, "\t\t\tx1: ", bb, "\t\t\tx2: ", x2)
                regularfalsi(x2, bb)
        else:
            print("Root is: ", x2)
    else:
        return 0


i = 0
j = 1
while (math.cos(i) - i*math.exp(i)) < 0:
    i += 1
while (math.cos(j) - j*math.exp(j)) > 0:
    j -= 1
x0 = i-1
x1 = j+1
regularfalsi(0, 1)
