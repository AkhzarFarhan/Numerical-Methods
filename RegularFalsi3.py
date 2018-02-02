import sys
import math
sys.setrecursionlimit(1000000000)


def regularfalsi(ab, bb):
    if abs(ab-bb) > 0.00001:
        x2 = ab - ((bb-ab)*(ab*math.log10(ab)-1.2)/((bb*math.log10(bb)-1.2)-(ab*math.log10(ab)-1.2)))
        fx2 = x2*math.log10(x2)-1.2
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


i = 1
j = 4
while (i*math.log10(i)-1.2) < 0:
    i += 1
while (j*math.log10(j)-1.2) > 0:
    j -= 1
x0 = i-1
x1 = j+1
regularfalsi(x0, x1)
