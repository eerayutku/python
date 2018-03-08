deger = []
s = input("Bir cümle yada kelime giriniz : ")
s = s.lower()
deger += s
sira =[ii for n , ii in enumerate(deger) if ii not in deger[:n]]
d= "".join(sira)
print(d)