## **HW1 (1.yontem)** ##
```python
import random
sayi = 0
toplam = 0
a = [None] * 100
for i in range(1, 100):
    a[i] = i
a[0] = random.randint(1,99)
random.shuffle(a)
print(a)
for i in a:
    toplam = toplam + i
sayi = toplam - 4950
print("random:",sayi)
```
> 'sayi' ve 'toplam' adinda iki degisken tanimladim. Daha sonra 'a' dizisi tanimlayip 100'e kadar olan sayilari ekledim. Daha sonra bu sayilari 'shuffle' ile karistirdim. Bir dongu olustutup bu sayilari toplattim. Karisan sayilarda fazladan bir sayi oldugu icin bu toplamdan fazla cikti. Cikan sayiyi toplamdan cikararak duplicate sayiyi buldum.

## **HW1 (2.yontem)** ##
```python
import random
sayi = 0
arr = [None] * 100
for i in range(1, 100):
    arr[i] = i
    arr2 = i
arr[0] = random.randint(1, 99)
print(arr)
random.shuffle(arr)
randoms = [x for n, x in enumerate(arr) if x in arr[:n]]
print ("Random:", randoms)
```
> Cogu kismi 1.yontem ile tek farkı son kisimda 'enumerate' komudunu calistirmamiz. Bu kod ile birlikte arr dizisindeki elemanlara bir deger atiyoruz. Daha sonra dizide bulunan her eleman icin deger atinca bir eleman fazla cikiyor. Bu fazla cikan eleman duplicate olan sayi olmus oluyor.

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
deger = []
s = input("Bir cümle yada kelime giriniz : ")
s = s.lower()
deger += s
sira =[ii for n , ii in enumerate(deger) if ii not in deger[:n]]
d= "".join(sira)
print(d)
```
> Kullaniciya bir kelime girdiyoruz. Girdilen kelimeyi 'lowercase' işlemine soktum. Cunku ASCII çetelesinde buyuk harf ve kucuk harf farkı oldugundan buyuk kucuk duplicate harfleri cikarmiyordu. Daha sonra girilen degeri degiskene atadim. Daha sonra yine 'enumerate' kullanarak dizideki elemanlara sayi atadim. En son da bu degerleri join ederek yazdirdim.

## **HW4** ##
```python
s = input("Lütfen bir kelime giriniz:")
length = len(s)
i = 0
while i < length / 2 + 1:
    if s[i] != s[-i - 1]:
        print("Girdiğiniz kelime palindrom degildir")
        break
    i += 1
else:
    print("Girdiginiz kelime palindromdur.")
```
> Kullaniciya bir deger girmesini istiyoruz. Bu girilen sayinin uzunlugunu aliyoruz. Bu uzunluğu donguye sokarak kelimenin tersi ile aynı olup olmadigini kontrol ediyoruz.
