## **HW1 (1.yontem)** ##
```python
import random
sayi = 0
ilktoplam = 0
toplam = 0
a = [None] * 100
for i in range(1, 100):
    a[i] = i
    ilktoplam = ilktoplam + i
a[0] = random.randint(1,99)
random.shuffle(a)
print(a)
for i in a:
    toplam = toplam + i
sayi = toplam - ilktoplam
print("random:",sayi)
```
> 'sayi' ve 'toplam' adinda iki degisken tanimladim. Daha sonra 'a' dizisi tanimlayip 100'e kadar olan sayilari ekledim. Daha sonra bu sayilari 'shuffle' ile karistirdim. Bir dongu olustutup bu sayilari toplattim. Karisan sayilarda fazladan bir sayi oldugu icin bu toplamdan fazla cikti. Cikan sayiyi toplamdan cikararak duplicate sayiyi buldum.

## **HW1 (2.yontem)** ##
```python
import random
arr = [None] * 100
temparr = [None] * 100
for i in range(1, 100):
    arr[i] = i
arr[0] = random.randint(1,99)
random.shuffle(arr)
print(arr)
for i in arr:
    d = temparr[i]
    if d == None:
        temparr[i-1]=1
    else:
        print("random: {}".format(i))
        break
```
> İki tane dizi actim. İlk dizide sayilari karistirarak sayilari diziye ekledim. Ikinci diziye de bu sayilarin olup olmadigini kontrol ediyorum. Birinci dizide olan sayilarin yeri ikinci sayida da dolduruluyor. Hepsi doldurulunca geriye bir tane fazla sayi kaliyor. Bu fazla sayi duplicaye olmus oluyor.

## **HW2** ##
```python
kelime = input("Bir kelime giriniz:")
a = int(input("Baslangic sayisini giriniz:"))
b = int(input("Sonlandirma sayisini giriniz(Kelimedeki harf sayısından büyük olmamalıdır.):"))
print("kelime[:a]+ kelime[b:]: {}".format(kelime[:a]+kelime[b:]))
```
> Kullaniciya kelime, baslangic sayisi ve sonlandirma sayisi girdiriyoruz. Daha sonra ':a' ve 'b:' kodlarıyla girilen baslangic sayisindan onceki harfleri ve girilen sonlandirma sayisindan sonraki degerleri ekrana yazdirdim.

## **HW3** ##
```python
a=[]
s= input("Bir cümle ya da kelime giriniz:")
s = s.lower()
tmp=[None] * len(s)
i = 0
for c in s:
    print(c)
    varmi = False
    for j in range(0,i):
        k = tmp[j]
        if c == k:
            varmi = True
    if varmi == False:
        tmp[i]=c
        i = i+1
print(tmp)
```
> Kullaniciya bir kelime girdiyoruz. Girdilen kelimeyi 'lowercase' işlemine soktum. Cunku ASCII çetelesinde buyuk harf ve kucuk harf farkı oldugundan buyuk kucuk duplicate harfleri cikarmiyordu. Daha sonra girilen degeri degiskene atadim. For içerisinde for acarak 'varmi' diye bir degisken tanimladim. Girilen kelimedeki harfleri bir diziye sokarak harfleri listeledim. Daha sonra bu harfleri bir diziye aktardim. Daha sonra kelimeleri diziye aktarirken bu harfin dizinin içerisinde olup olmadiginin kontrolunu yaptim.

## **HW4** ##
```python
a = input("Bir kelime giriniz:")
if len(a) % 2 == 0:
    print("palindrom degildir")
else:
    ort = len(a)/2
    s = round(ort)-1
    palindrom = True
    for i in range(0,s):
        if a[0-(i+1)] != a[i]:
             print("palindrom degildir")
             palindrom = False
             break
    if palindrom:
             print("palindromdur")
```
> Girilen kelimenin uzunlugunun oncelikle cift veya tek sayi oldugunu kontrol ettim. Uzuluk ciftse girilen kelime palindrom olmaz. Eger bu sayi tek ise isleme sokulur. Bu islemde oncelikle uzunlugu ikiye boldum. Daha sonra 'round(ort)' komutuyla bu sayiyi yukariya yuvarladim. 0'dan girilen kelimenin ortasindaki harfin degerine kadar donguyu calistirdim. Daha sonra ortanca sayinin onceki kismi ile(1,2,3) sonraki kısmının(-1,-2,-3) eşit olup olmadigini kontrol ettim. Eger esit degilse kelime palindrom degildir. Eger bu degerler esit ise sayi palindromdur.
