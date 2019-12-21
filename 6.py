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
        yenikalan = kalansayilar[kalansayilar.index(i)+ 1:]
        yenieldeki = eldeki.copy()
        yenieldeki.append(i)
        altkume(yenikalan, yenieldeki)

altkume(liste, [])

print(diziler)