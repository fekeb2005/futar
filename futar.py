# 1. feladat
t = open("tavok.txt","r")
tavok = []
for x in t:
	tav = x.split(" ")
	tav[0] = int(tav[0])
	tav[1] = int(tav[1])
	tav[2] = int(tav[2])
	tavok.append(tav)
# print(tavok)
t.close()

# 2. feladat
print("\n2. feladat")
def sort_tavok (e):
	return (e[0] * 100) + e[1]
tavok.sort(key=sort_tavok)
print(tavok[0][2], "km")

# 3. feladat
print("\n3. feladat")
print(tavok[-1][2], "km")

# 4. feladat
print("\n4. feladat")
napok = []
for i in range(1, 8): napok.append(i)
for tav in tavok:
	if tav[0] in napok:
		napok.remove(tav[0])
print(*napok, sep=", ")

# 5. feladat
print("\n5. feladat")
max = 0
nap = 0
for i in range(1, 8):
	napi_max = 0
	for tav in tavok:
		if tav[0] == i:
			napi_max += 1
	if napi_max > max:
		max = napi_max
		nap = i
print(nap)

# 6. feladat
print("\n6. feladat")
for i in range(1, 8):
	napi = 0
	for tav in tavok:
		if tav[0] == i:
			napi = napi + tav[2]
	print(f'{i}. nap: {napi} km')

# 7. feladat
print("\n7. feladat")
def dij(d):
	if 1 <= d <= 2:
		return 500
	if 3 <= d <= 5:
		return 700
	if 6 <= d <= 10:
		return 900
	if 11 <= d <= 20:
		return 1400
	if 21 <= d <= 30:
		return 2000
print(dij(int(input("Tav: "))))

# 8. feladat
tavok.sort(key=sort_tavok)
f = open("dijazas.txt", "w")
for tav in tavok:
	# print(f'{tav[0]}. nap {tav[1]}. ut: {dij(tav[2])} Ft')
	f.write(f'{tav[0]}. nap {tav[1]}. ut: {dij(tav[2])} Ft\n')
f.close()

# 9. feladat
print("\n9. feladat")
fizets = 0
for tav in tavok:
	fizets = fizets + dij(tav[2])
print(fizets, "Ft")