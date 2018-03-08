kelime = input("Bir kelime giriniz:")
a = int(input("Baslangic sayisini giriniz:"))
b = int(input("Sonlandirma sayisini giriniz(Kelimedeki harf sayısından büyük olmamalıdır.):"))
print("kelime[:a]+ kelime[b:]: {}".format(kelime[:a]+kelime[b:]))