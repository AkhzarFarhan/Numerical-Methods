import math


def f(x):
    return x*math.log10(x) - 1.2


def regularfalsi(x0, x1, x_count):
    r_count = x_count + 1
    x2 = x0 - (((x1-x0)*f(x0))/(f(x1)-f(x0)))
    if f(x2) > 0:
            print("x0: ", x0, "\t\t\tx1: ", x1, "\t\t\tx2: ", x2)
            if r_count > 10:
                print("\n\n\nApproximate root is: ", x2)
                return 0
            else:
                regularfalsi(x0, x2, r_count)
    elif f(x2) < 0:
            print("x0: ", x0, "\t\t\tx1: ", x1, "\t\t\tx2: ", x2)
            if r_count > 10:
                print("\n\n\nApproximate root is: ", x2)
                return 0
            else:
                regularfalsi(x2, x1, r_count)


count = 0
i = 1
j = 4
while f(i) < 0:
    i += 1
while f(j) > 0:
    j -= 1
a = i-1
b = j+1
regularfalsi(a, b, count)
