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
