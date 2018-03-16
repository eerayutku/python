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

