def f(x):
    return x**3 - x - 1


def minimiser(a, b):
    mi = 0.1
    mj = 0.1
    while f(a+mi) < 0:
        mi += 0.1
    while f(b-mj) > 0:
        mj += 0.1
    return [a+mi-0.1, b-mj+0.1]


def secant(xi):
    xi.append((xi[-2]*f(xi[-1]) - xi[-1]*f(xi[-2]))/(f(xi[-1]) - f(xi[-2])))
    while True:
        if abs(xi[-1] - xi[-2]) > 0.00001:
            print("xi: ", xi[-1])
            secant(xi)
        else:
            break


i = 0
j = 9
while (f(i)) < 0:
    i += 1
while (f(j)) > 0:
    j -= 1
secant(minimiser(i-1, j+1))
