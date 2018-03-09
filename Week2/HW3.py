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
