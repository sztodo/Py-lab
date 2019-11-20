from math import *

def rezolvare_triunghi(a, b, c):
    p = (a + b+ c) / 2
    S = sqrt(p * (p - a) * (p - b) * (p - c))
    print('Aria triunghiului este ', S)
    print('Inaltimea 1 = ', 2 * S / a)
    print('Inaltimea 2 = ', 2 * S / b)
    print('Inaltimea 3 = ', 2 * S / c)
    A = acosh((pow(b, 2) + pow(c, 2) - pow(a, 2)) / 2 * b * c)
    B = acosh((pow(a, 2) + pow(c, 2) - pow(b, 2)) / 2 * a * c)
    C = acosh((pow(b, 2) + pow(a, 2) - pow(c, 2)) / 2 * b * a)
    if A == B or A == C or B == C:
        if A == B == C:
            print('Triunghi echilateral')
        else:
            print('Triunghi isoscel')
        if A == 45. or B == 45.:
            print('Triunghi dreptunghic isoscel')
    elif A == 90. or B == 90. or C == 90.:
        print("triunghi dreptunghic")
    else:
        print("triunghi oarecare")


if __name__ == '__main__':
    a = eval(input('a='))
    b = eval(input('b='))
    c = eval(input('c='))
    rezolvare_triunghi(a, b, c)
