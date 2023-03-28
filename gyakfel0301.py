#                      0          1         2          3        4
nevek:list[str] = ['Richárd', 'Dániel', 'Borbála', 'Zsuzsa', 'Judit']

# feladatok 3.1.a
for nev in nevek:
    print(nev)

# feladatok 3.1.b
magassagok:list[int] = []
for x in range(len(nevek)):
    m:int = int(input(f'írd be {nevek[x]} magasságát: '))
    magassagok.append(m)

# feladatok 3.1.c
osszeg:int = 0
for magassag in magassagok:
    osszeg += magassag
atlag_magassak = osszeg / len(magassagok)
print(f'az átlagmagasság: {atlag_magassak} cm')

# feladatok 3.1.d
# nevek.sort()
# print(nevek)

# feladatok 3.1.e

maximum_index:int = 0
for index in range(1, len(magassagok)):
    if magassagok[index] > magassagok[maximum_index]:
        maximum_index = index

print(f'a legmagasabb {nevek[maximum_index]}, ő {magassagok[maximum_index]} cm')

# mindkét lista rendezése magasságok alapján (hardcore mode ON)
for i in range(len(magassagok) - 1):
    for j in range(i + 1, len(magassagok)):
        if magassagok[i] > magassagok[j]:
            sm:int = magassagok[i]
            magassagok[i] = magassagok[j]
            magassagok[j] = sm
            sn:str = nevek[i]
            nevek[i] = nevek[j]
            nevek[j] = sn

print('magasságok szerint rendezve:')
for i in range(len(nevek)):
    print(f'{nevek[i]}: {magassagok[i]} cm')
