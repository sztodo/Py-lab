from math import sqrt
def patrat_cerc(R):
    print(R)
    l = 2*R/sqrt(2)
    print(l)


n = eval(input('n='))
R = eval(input('R='))

while n!=0:
    patrat_cerc(R)
    R = R/sqrt(2)
    n = n-1

