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
