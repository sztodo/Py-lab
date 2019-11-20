x = eval(input('x='))
n = eval(input('n='))
d = eval(input('durata='))
distanta = x
while d!=0 and x>=1:
    d = d - n
    x = x/2
    distanta = distanta + x
print('Magarusul a parcurs ', format(distanta, '.2f'))