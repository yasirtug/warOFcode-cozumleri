sesliHarfler = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
a = input()

dizi = a.split()

for kelime in dizi:
    lastSesliIndex = 0
    hata = False
    for harf in kelime:
        if(harf in sesliHarfler):
            if(sesliHarfler.index(harf) < lastSesliIndex):
                hata = True
                break
            else:
                lastSesliIndex = sesliHarfler.index(harf)
    if(not hata):
        print(kelime)