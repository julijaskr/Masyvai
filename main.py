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
