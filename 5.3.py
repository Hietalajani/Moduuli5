luku = int(input('Anna luku: '))

x = 3
alkuluku = False

for jakaja in range(luku-1):
    if x <= luku-1:
        if luku % 2 == 0:
            alkuluku = True
            break
        elif luku % x == 0:
            alkuluku = True
            break
        else:
            x += 2
    else:
        break

if alkuluku:
    print(f'{luku} ei ole alkuluku.')
elif not alkuluku and luku != 1:
    print(f'{luku} on alkuluku.')
else:
    print('YRITÄTSÄ HUIJATA HÄ')
