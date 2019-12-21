liste = input("sayi listesi: ").split()
liste = list(map(int, liste))

diziler = []
olacaktoplam = int(input("istenen toplam: "))

def altkume(kalansayilar, eldeki):
    toplam = 0
    for i in eldeki:
        toplam += i
    if(toplam == olacaktoplam):
        diziler.append(eldeki)
    for i in kalansayilar:
        yenikalan = kalansayilar.copy()
        yenikalan.remove(i)
        yenieldeki = eldeki.copy()
        yenieldeki.append(i)
        altkume(yenikalan, yenieldeki)

altkume(liste, [])
resultdizi = []
var = False
for i in diziler:
    var = False
    for j in resultdizi:
        if(set(i) == set(j)):
            var = True
    if(not var):
        resultdizi += [i]
print(resultdizi)