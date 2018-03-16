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
> İki tane dizi actim. İlk dizide sayilari karistirarak sayilari diziye ekledim. Ikinci diziye de bu sayilarin olup olmadigini kontrol ediyorum. Birinci dizide olan sayilarin yeri ikinci sayida da dolduruluyor. Hepsi doldurulunca geriye bir tane fazla sayi kaliyor. Bu fazla sayi duplicate olmus oluyor.

## **HW2** ##
```python
kelime = input("Bir Kelime Giriniz : ")
a = int(input("Başlangıç Sayısını Giriniz : "))
b = int(input("Bitiş Sayısını Giriniz : "))
if a > len(kelime) or b > len(kelime):
    print("Kelimeden Büyük Değer Girilemez!")
else:
    if a <= 0 or b <= 0:
        print("Sıfır Girilemez!")
    else:
        a = a-1
        print("Girdiğiniz Kelime : ", kelime)
        print("Kesilmiş Kelime : {}".format(kelime[:a]+kelime[b:]))
```
> Kullaniciya kelime, baslangic sayisi ve sonlandirma sayisi girdiriyoruz. Daha sonra ':a' ve 'b:' kodlarıyla girilen baslangic sayisindan onceki harfleri ve girilen sonlandirma sayisindan sonraki degerleri ekrana yazdirdim. 'if' kisimlarinda ise girilen baglangic ve sonlandirma sayilarinin gerekli kurallar icerisinde girilmesini sagladim. Bu kurallar girilen sayinin girilen kelimenin uzunlugundna buyuk olmamasi ve sifir girilememesidir. 'a = a-1' kisminda ise dizilerin ilk degeri sifira atandigi icin bunu engellemis oldum.

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
a = input("Bir kelime giriniz : ")
a=a.lower()
arr=[]
arr2=[]
for e in range(len(a)):
    arr.append(a[e])
    arr2.append(a[e])
ort=len(a)/2
ort=int(ort)
for i in range (0,ort):
    arr[i], arr[0 - (i + 1)] = arr[0 - (i + 1)], arr[i]
if arr==arr2:
    print("Palindromdur.")
else:
    print("Palindrom değildir.")
```
> Kullanıcıya kelime girdisi yaptırdım. Daha sonra girilen kelimedeki harfleri küçülttüm. İki dizi oluşturdum. Girilen kelimenin uzunluğu kadar dönecek bir for döngüsü oluşturdum. Bu girilen harfleri diziye aktardım. Daha sonra girilen kelimeyi ikiye bölerek ortanca harfi buldum. Bulduğum ortanca harfe dönecek kadar bir for döngüsü daha oluşturdum. Bu for döngüsünde ortanca harfin sağındaki ve solundaki harflerin yerini değiştirdim. Son olarak da iki dizye aktarılan harflerin yerleri aynıysa palindrom yazmasını, değil ise palindrom değildir yazmasını sağladım.
