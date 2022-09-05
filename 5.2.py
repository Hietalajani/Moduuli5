luku = input('Anna luku: ')

luvut = []

while luku != "":
    luku = int(luku)
    luvut.append(luku)
    luku = input('Anna luku: ')

luvut.sort(reverse=True)
print(f'5 suurinta: {luvut[0:5]}.')
