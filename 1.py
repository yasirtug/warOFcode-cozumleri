a = input("saat:dakika giriniz: ").split(':')
saat = int(a[0])
dakika = int(a[1])

saat %= 12
saatAci = (360 / 12.0) * saat
dakikaAci = (360 / 60.0) * dakika
aci = 180 - abs(abs(saatAci - dakikaAci) - 180);
print(int(aci))