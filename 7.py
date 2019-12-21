kolonlar = input().split()
kolonlar = list(map(int, kolonlar))

suSeviyeleri = kolonlar.copy()

maximumSeviye = max(kolonlar)
guncelSeviye = 0
index = 0
for seviye in kolonlar:
    if(seviye > guncelSeviye):
        guncelSeviye = seviye
    suSeviyeleri[index] = guncelSeviye
    index += 1

suSeviyeleri.reverse()
kolonlar.reverse()

guncelSeviye = 0
index = 0
for seviye in kolonlar:
    if(seviye == maximumSeviye):
        break
    if(seviye > guncelSeviye):
        guncelSeviye = seviye
    suSeviyeleri[index] = guncelSeviye
    index += 1
su = 0
for i in range(0, len(suSeviyeleri)):
    su += suSeviyeleri[i] - kolonlar[i]
print(su)