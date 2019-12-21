n = int(input("agac sayisi: "))
agaclar = []
j = 0
for i in range(0, n):
    j += 1
    a = input(str(j) + ". agac: ").split()
    x = int(a[1])
    y = int(a[0])
    agaclar.append([x, y])

a = input("kişinin konumu: ").split()
bizimX = int(a[1])
bizimY = int(a[0])

minUzaklik = -1
index = -1
i = 0
for agac in agaclar:
    uzaklik = abs(bizimX - agac[0]) + abs(bizimY - agac[1])
    if(minUzaklik == -1 or uzaklik < minUzaklik):
        index = i
        minUzaklik = uzaklik
    i += 1
result = ''
agac = agaclar[index]
farkX = bizimX - agac[0]
farkY = bizimY - agac[1]

if(farkY > 0):
    result += str(abs(farkY)) + " birim yukarı "
elif(farkY < 0):
    result += str(abs(farkY)) + " birim aşağı "

if(farkX > 0):
    result += str(abs(farkX)) + " birim sola "
elif(farkX < 0):
    result += str(abs(farkX)) + " birim sağa "

result += "git."
if(len(result) == 4):
    print("gitme kal.")
else:
    print(result)