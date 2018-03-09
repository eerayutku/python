import random
arr = [None] * 100
temparr = [None] * 100
ilktoplam = 0
for i in range(1, 100):
    ilktoplam = ilktoplam + i
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
