## **HW1** ##
```python
class Calculator:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def infix2Postfix(self,infix):
        prec = {}
        prec["*"] = 2
        prec["/"] = 2
        prec["+"] = 1
        prec["-"] = 1
        self.Stack = Calculator()
        self.PostFix = []
        self.TempArr=[]
        self.infix=infix
        infix=infix.replace(" ","")
        inlen=len(infix)
        for arr in range (inlen):
            self.TempArr.append(infix[arr])
        for value in self.TempArr:
            if value in "0123456789":
                self.PostFix.append(value)
            else:
                while (not self.Stack.isEmpty()) and \
                 (prec[self.Stack.peek()] >= prec[value]):
                    self.PostFix.append(self.Stack.pop())
                self.Stack.push(value)
        while not self.Stack.isEmpty():
            self.PostFix.append(self.Stack.pop())
        return " ".join(self.PostFix)

inf=input("Infix giriniz : ")
pfix=Calculator().infix2Postfix(inf)
print("Postfix : "+pfix)
```
> Calculator adında bir adet class oluşturdum. Bu class'ın içerisine 'push,peek ve pop' methodlarını ekledim. Bu methodların
sonuna 'infix2Postfix' adında bir method oluşturdum. Method içerisine işlem önceliğini belirten değerlerini girdim. Çarpma ve bölme
işlemleri toplama ve çıkarma işlemlerine göre daha öncelikli olduğu için bu işlemlere 2 değerini atadım. Kalan toplama ve çıkarma işlemlerine
1 değerini atadım. Daha sonra Calculator classından çağırma işlemini gerçekleştiriyoruz. İki tane array oluşturuyorum. Girilen
değerin uzunluğunu alıyorum. Bu uzunluk değeri kadar dönecek bir for döngüsü oluşturuyor ve diziye(TempArr) atıyorum. Yazılan değerlerin
içerisinde rakamlar varsa bu girdileri de ikinci diziye(PostFix) atıyorum. Son olarak da postfixi oluşturduktan sonra ekrana
yazdırıyoruz.
