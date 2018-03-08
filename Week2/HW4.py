s = input("Lütfen bir kelime giriniz:")
length = len(s)
i = 0

while i < length / 2 + 1:
    if s[i] != s[-i - 1]:
        print("Girdiğiniz kelime palindrom degildir")
        break
    i += 1
else:
    print("Girdiginiz kelime palindromdur.")