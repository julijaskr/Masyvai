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
masyvas_3 = []
for i in range(10):
    sk_3 = random.randint(5, 25)
    masyvas_3.append(sk_3)
bendras_masyvas = masyvas + masyvas_3
print(bendras_masyvas)

# Iš masyvo elementų sukurkite du naujus masyvus. Vienas turi būti sudarytas iš neporinių indekso reikšmių, o kitas iš porinių
poriniai_indeksai= []
neporiniai_indeksai = []
for i in range(0, len(bendras_masyvas)):
    if i % 2 == 0:
        poriniai_indeksai.append(bendras_masyvas[i])
    else:
        neporiniai_indeksai.append(bendras_masyvas[i])
print("Poriniu indeksu reiksmes:", poriniai_indeksai)
print("Neporiniu indeksu reiksmes:", neporiniai_indeksai)

# Masyvo elementus su poriniais indeksais padarykite lygius 0 jeigu jie didesni už 15
for i in range(0,len(poriniai_indeksai)):
    if poriniai_indeksai[i] > 15:
        poriniai_indeksai[i] = 0
print("Su nuliais po pakeitimo:", poriniai_indeksai)

# Suraskite pirmą (mažiausią) indeksą, kurio elemento reikšmė didesnė už 10;
for i in range(0, len(neporiniai_indeksai)):
    if neporiniai_indeksai[i] >10:
        break
print(i)

# Sugeneruokite masyvą, kurio reikšmės atsitiktinės raidės A, B, C ir D, o ilgis 200. Suskaičiuokite kiek yra kiekvienos raidės.

# raidziu_masyvas = ['a','b','c','a']
# raides_skaiciavimas = {}
# for raide in raidziu_masyvas:
#     if raide in raides_skaiciavimas:
#         raides_skaiciavimas[raide] += 1
#     else:
#         raides_skaiciavimas[raide] = 1
# print(raides_skaiciavimas)

galimos_raides = ['a','b','c','d']
raidziu_masyvas = []
for raide in range(0,200):
    raides_pozicija = random.randint(0,len(galimos_raides)-1)
    raide = galimos_raides[raides_pozicija]
    raidziu_masyvas.append(raide)
for raide in galimos_raides:
     print(f"Raide {raide} pasikartojo: {raidziu_masyvas.count(raide)}")
print(raidziu_masyvas)

# Išrūšiuokite raidziu masyvą pagal abecėlę
galimos_raides = ['a','b','c','d']
raidziu_masyvas = []
for raide in range(0,200):
    raides_pozicija = random.randint(0,len(galimos_raides)-1)
    raide = galimos_raides[raides_pozicija]
    raidziu_masyvas.append(raide)
raidziu_rusiavimas = sorted((raidziu_masyvas))
print(raidziu_rusiavimas)
print("+++++++=")
# Sugeneruokite 3 masyvus pagal 3 uždavinio sąlygą. Sudėkite masyvus, sudėdami atitinkamas reikšmes. Paskaičiuokite kiek unikalių reikšmių kombinacijų gavote
# galimos_raides = ['a','b','c','d']
# galimos_raides_2 = ['a','b','c','d']
# galimos_raides_3 = ['a','b','c','d']
# raidziu_masyvas = []
# raidziu_masyvas_2 = []
# raidziu_masyvas_3 = []
bendras_raidziu_masyvas = []
# unikali_reiksme = []
# reiksmiu_sk = 0
# for raide_1 in range(0,200):
#     raides_pozicija = random.randint(0,len(galimos_raides)-1)
#     raide_1 = galimos_raides[raides_pozicija]
#     raidziu_masyvas.append(raide_1)
# for raide_2 in range(0,200):
#     raides_pozicija_2 = random.randint(0,len(galimos_raides_2)-1)
#     raide_2 = galimos_raides_2[raides_pozicija_2]
#     raidziu_masyvas_2.append(raide_2)
# for raide_3 in range(0,200):
#     raides_pozicija_3 = random.randint(0,len(galimos_raides_3)-1)
#     raide_3 = galimos_raides_3[raides_pozicija_3]
#     raidziu_masyvas_3.append(raide_3)
# for raide_1, raide_2, raide_3 in zip(raidziu_masyvas, raidziu_masyvas_2, raidziu_masyvas_3):
#     bendras_raidziu_masyvas.append((raide_1 + raide_2 + raide_3))
#
# print(bendras_raidziu_masyvas)
#
# for derinys in bendras_raidziu_masyvas:
#     if derinys in reiksmiu_sk:
#         reiksmiu_sk[derinys] += 1
#     else:
#         reiksmiu_sk = 1
# print(len(unikali_reiksme))

# reiksmiu_skaicius = {}
#
# for reiksme in bendras_raidziu_masyvas:
#     reiksmiu_skaicius[reiksme] = reiksmiu_skaicius.get(reiksme, 0) + 1
#
# print("Unikalios reikšmės ir jų pasikartojimai:")
# for reiksme, kiekis in reiksmiu_skaicius.items():
#     print(f"{reiksme}: {kiekis}")

galimos_raides = ['a', 'b', 'c', 'd']

# Trys masyvai
raidziu_masyvas_1 = []
raidziu_masyvas_2 = []
raidziu_masyvas_3 = []

# Užpildome kiekvieną masyvą 200 atsitiktinėmis raidėmis
for _ in range(200):
    raidziu_masyvas_1.append(random.choice(galimos_raides))
    raidziu_masyvas_2.append(random.choice(galimos_raides))
    raidziu_masyvas_3.append(random.choice(galimos_raides))

# Sudedame atitinkamas reikšmes iš trijų masyvų
bendras_masyvas = []
for r1, r2, r3 in zip(raidziu_masyvas_1, raidziu_masyvas_2, raidziu_masyvas_3):
    bendras_masyvas.append(r1 + r2 + r3)

# Suskaičiuojame kiekvienos unikalios reikšmės pasikartojimus
reiksmiu_skaicius = {}

for reiksme in bendras_masyvas:
    reiksmiu_skaicius[reiksme] = reiksmiu_skaicius.get(reiksme, 0) + 1

# Atspausdiname unikalias reikšmes ir jų pasikartojimus
print("Unikalios reikšmės ir jų pasikartojimai:")
for reiksme, kiekis in reiksmiu_skaicius.items():
    print(f"{reiksme}: {kiekis}")

# Sugeneruokite du masyvus, kurių reikšmės yra atsitiktiniai skaičiai nuo 100 iki 999. Masyvų ilgiai 100. Masyvų reikšmės turi būti unikalios savo masyve (t.y. neturi kartotis).
masyvas_1 = []
masyvas_2 = []

for i in range(100):
    sk_6 = random.randint(100,999)
    masyvas_1.append(i)
print(masyvas_1)