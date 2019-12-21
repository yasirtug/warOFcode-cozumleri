toplamolacakki = int(input("istenen toplam: "))
sayilar = input("sayilar: ").split()
sayilar = list(map(int, sayilar))


def islem(kalanSayilar, eldekiSayilar):

    if(len(kalanSayilar) == 0):
        if(sum(eldekiSayilar) == toplamolacakki):
            print(eldekiSayilar)
        return
    newKalan = kalanSayilar.copy()
    newEldeki1 = eldekiSayilar.copy()
    newEldeki2 = eldekiSayilar.copy()
    siradakiSayi = newKalan[0]

    del newKalan[0]
    newEldeki1.append(siradakiSayi)
    newEldeki2.append(-siradakiSayi)
    islem(newKalan, newEldeki1)
    islem(newKalan, newEldeki2)

islem(sayilar, [])