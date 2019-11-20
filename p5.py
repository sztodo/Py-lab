def borne(altitudine1, altitudine2):
    return altitudine2 - altitudine1

n = eval(input('n='))
a = eval(input('altitudine 1 ='))
d = eval(input('distanta 1 ='))
l = 0
for i in range(1, n):
    alt = eval(input('altitudine = '))
    dist = eval(input('distanta = '))
    if borne(a, alt) > l:
        l = borne(a, alt)
        maxd = dist
    a =alt
    d = dist
print(maxd)
