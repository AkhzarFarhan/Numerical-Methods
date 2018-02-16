# from sympy import *
# y = symbols('y')
# init_printing(use_unicode=True)


def f(x):
    return x**3 - 3*x + 1


def fd(yi):
    # return diff(f(yi), y)
    return 3*(yi**2 - 1)


def nr(a):
    a.append(a[-1] - (f(a[-1])/fd(a[-1])))
    while True:
        if abs(a[-1] - a[-2]) > 0.00001:
            print("xi: ", a[-1])
            nr(a)
        else:
            break


aMain = [0.3, 0.3, 0.3]
nr(aMain)
