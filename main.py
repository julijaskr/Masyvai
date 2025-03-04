import random

# Sugeneruokite masyvą iš 30 elementų (indeksai nuo 0 iki 29), kurių reikšmės yra atsitiktiniai skaičiai nuo 5 iki 25.
masyvas = []
for sk in range(0,30):
    sk = random.randint(5, 25)
    masyvas.append(sk)
print(masyvas)

# Suskaičiuokite kiek masyve yra reikšmių didesnių už 10
sk_didenis_10 = 0
for sk in masyvas:
    if sk > 10:
        sk_didenis_10 += 1
print("Didesniu nei 10 yra: ", sk_didenis_10)

# Raskite didžiausią masyvo reikšmę
max_reiksme = masyvas[0]
for sk in  masyvas:
    if sk > max_reiksme:
        max_reiksme = sk
print(max_reiksme)

# Suskaičiuokite visų reikšmių sumą
reiksmiu_suma = 0
for sk in masyvas:
    reiksmiu_suma += sk
print("Reiksmiu suma:", reiksmiu_suma)

# Sukurkite naują masyvą, kurio reikšmės yra 1 uždavinio masyvo reikšmes minus tos reikšmės indeksas
masyvas_2 = []
for i in range(0, len(masyvas)):
    masyvas_2.append(masyvas[i] - i)
print(masyvas_2)

# Papildykite masyvą papildomais 10 elementų su reikšmėmis nuo 5 iki 25, kad bendras masyvas padidėtų iki indekso 39