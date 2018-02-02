import sys
sys.setrecursionlimit(1000000000)


def regularfalsi(ab, bb):
    if abs(ab-bb) > 0.00001:
        x2 = ab - ((bb-ab)*(ab**3 - 2*ab - 5)/((bb**3 - 2*bb - 5)-(ab**3 - 2*ab - 5)))
        fx2 = x2**3 - 2*x2 - 5
        if fx2 > 0:
                print("x0: ", ab, "||\t\t\tx1: ", bb, "||\t\t\tx2: ", x2)
                regularfalsi(ab, x2)
        elif fx2 < 0:
                print("x0: ", ab, "||\t\t\tx1: ", bb, "||\t\t\tx2: ", x2)
                regularfalsi(x2, bb)
        else:
            print("Root is: ", x2)
    else:
        return 0


i = 0
j = 5
while (i**3 - 2*i - 5) < 0:
    i += 1
while (j**3 - 2*j - 5) > 0:
    j -= 1
x0 = i-1
x1 = j+1
regularfalsi(x0, x1)
