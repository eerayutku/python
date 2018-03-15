> Geçen haftanın ödevleri güncellenmiş bir şekilde Week2 klasörünün içerisindedir.

## **HW1** ##
```python
def rvs(kelime):
    harfler = []
    for i in range(len(kelime)):
        harfler.append(kelime[i])
    for j in range(int(len(harfler) / 2)):
        harfler[j], harfler[len(harfler) - 1 - j] = harfler[len(harfler) - 1 - j], harfler[j]
    return harfler
var = input("kelime veya cümle gir:")
print(rvs(var))
```
> Öncelikle bir fonksiyon oluşturdum. Daha sonra harfler adında bir dizi oluşturdum. Diziden sonra girilen kelimenin uzunluğu kadar dönecek bir for döngüsü oluşturdum. Bu diziye girilen kelimedeki harfleri ekledim. Daha sonra ikinci bir for döngüsü oluşturdum.
Bu for döngüsü dizinin uzunluğunun yarısı kadar dönecek. Kelimenin harflerini tersine çevirdim. Daha sonra girilen kelimenin tersini ekrana bastırdım.
