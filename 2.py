a = input()

dizi = a.split()

result = []

def karsilastir(kelime1, kelime2):
    kelime1dizi = [0] * 300
    kelime2dizi = [0] * 300
    for i in kelime1:
            kelime1dizi[ord(i) - ord('a')] += 1
    for i in kelime2:
            kelime2dizi[ord(i) - ord('a')] += 1
    result = True
    for i in range (0, 25):
        if(kelime1dizi[i] != kelime2dizi[i]):
            result = False
    return result

for i in range(1, len(dizi)):
    for j in range(0, i):
        if(karsilastir(dizi[i], dizi[j])):
            if(dizi[i] != dizi[j]):
                result.append((dizi[i], dizi[j]))

print(result)
