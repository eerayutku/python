dongu = int(input("Dongu sinirini belirleyiniz")
for i in range(0,dongu) :
    birincisayi = int(input("Birinci sayıyı giriniz:"))
    ikincisayi = int(input("İkinci sayiyi giriniz:"))
    islem = input("Yapacağınız işlemi seçiniz(+,-,/,*):")
    if islem == "+" :
        print (birincisayi+ikincisayi)
    elif islem == "-" :
        print (birincisayi-ikincisayi)
    elif islem == "*" :
        print (birincisayi*ikincisayi)
    elif (islem == "/") & (ikincisayi==0):
        print ("Gecerli bir sayi girisi yapiniz")
    elif islem =="/" :
        print (birincisayi/ikincisayi)
    elif islem == "exit":
        break
    else:
        print("Lütfen belirtilen operatörlerden birini giriniz")
