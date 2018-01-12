def bisection(ab, bb):
    if abs(ab-bb) > 0.0000001:
        mid = (ab+bb)/2
        fx = mid**3 - 4*mid - 9
        if fx > 0:
                print("a: ", ab, "||\t\t\tb: ", bb, "||\t\t\tfx: ", fx)
                bisection(ab, mid)
        elif fx < 0:
                print("a: ", ab, "||\t\t\tb: ", bb, "||\t\t\tfx: ", fx)
                bisection(mid, bb)
        else:
            print("Root is: ", mid)
    else:
        return 0


i = 0
j = 5
while (i**3 - 4*i - 9) < 0:
    i += 1
while (j**3 - 4*j - 9) > 0:
    j -= 1
bisection(i-1, j+1)
