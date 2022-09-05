import random
arpa = int(input('Anna noppien määrä: '))

nopat = []

for noppa in range(arpa):
    silmaluku = random.randint(1, 6)
    print(silmaluku)
    nopat.append(silmaluku)

print(f'Silmälukujen summa: {sum(nopat)}.')

# Vaihtoehtoinen ratkaisutapa

summa = 0

for noppa in range(arpa):
    luku = random.randint(1, 6)
    summa += luku

print(f'Silmälukujen summa: {summa}.')