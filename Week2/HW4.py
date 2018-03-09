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
