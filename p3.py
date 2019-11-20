x = eval(input('Screti elementele codului cu virgula intre ele'))  # citirea codului
p = 1  # initializam produsul numerelor pare cu 1
s = 0  # initializam suma numerelor impare cu 0
for number in x:
    if number % 2 == 0:
        p = p * number
    else:
        s = s + number
if p % x[0] == s % x[0]:
    print('CORECT')
else:
    print("INCORECT")
