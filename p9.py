n = eval(input('n='))
sec = n % 60
mint = n // 60
ore = mint //60
mint = mint % 60
zile = ore // 24
ore = ore % 24
ani = zile // 365
zile = zile % 365
zile_bis = ani // 4
if zile >= zile_bis:
    zile -= zile_bis
else:
    ani -=1
    zile += 365
    zile -=zile_bis
if zile > 30:
    luni = zile // 30
    zile = zile % 30
print(ani, ' de ani,', 'aproximativ', luni, 'luni,', zile, ' zile, ', ore, ' ore,', mint, ' minute, ', sec, ' secunde.' )
