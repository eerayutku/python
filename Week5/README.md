## **HW1** ##
```python
class Node:
    def __init__(self, data):
        self._data = data
        self._nextNode = None

    @property
    def data(self):
        return self._data

    @property
    def nextNode(self):
        return self._nextNode

    @nextNode.setter
    def nextNode(self, value):
        self._nextNode = value


class LinkedList:
    def __init__(self):
        self._rootNode = None

    def add(self, data):
        tmp = Node(data)
        if self._rootNode == None:
            self._rootNode = tmp
            return
        v = self._rootNode
        while v.nextNode != None:
            v = v.nextNode
        v.nextNode = tmp

    def dump(self):
        if self._rootNode == None:
            return
        v = self._rootNode
        while v != None:
            print(v.data)
            v = v.nextNode

    def delete(self, data):
        if self._rootNode == None:
            return
        if self._rootNode.data == data:
            self._rootNode = self._rootNode.nextNode
            return
        v1 = self._rootNode
        v2 = v1.nextNode
        while v2 != None:
            if v2.data == data:
                v1.nextNode = v2.nextNode
                return
            v1 = v2
            v2 = v2.nextNode

    def findMid(self):
        if self._rootNode == None:
            print("LinkedList boştur.")
            return
        if self._rootNode.nextNode == None:
            print("LinkedList tek elemanlıdır.")
            return
        if self._rootNode.nextNode != None and self._rootNode.nextNode.nextNode == None:
            print("LinkedList 2 elemanlıdır orta elemanı yoktur.")
            return
        slowptr = self._rootNode
        fastptr = slowptr.nextNode
        while fastptr != None:
            try:
                slowptr = slowptr
                fastptr = fastptr.nextNode
                slowptr = slowptr.nextNode
                fastptr = fastptr.nextNode
            except AttributeError:
                print("Linkedlist uzunluğu çift sayıdır. Ortada 2 eleman vardır.")
                double = self._rootNode
                double2 = double.nextNode
                while double2 != slowptr:
                    double = double2
                    double2 = double2.nextNode
                print("Ortadaki Eleman : ", double.data)
        print("Ortadaki Eleman : ", slowptr.data)


if __name__ == "__main__":
    import random

    print("--" * 10)
    a = LinkedList()
    a.add(5)
    a.add(10)
    a.add(15)
    a.add(20)
    a.add(25)
    a.add(30)
    a.add(35)
    a.add(40)
    a.dump()
    print("--" * 10)
    a.findMid()
    print("--" * 10)
    b = LinkedList()
    x = random.randint(1, 100)
    print("Oluşturulan random linkedlist", x, "Elemanlıdır.")
    for i in range(x):
        b.add(random.randint(1, 100))
    b.dump()
    print("--" * 10)
    b.findMid()
    print("--" * 10)
```
> Derste oluşturmuş olduğumuz sınıflara(Node ve Linkedlist) ve methodlara(add,dump,delete) ek olarak 'FindMid' adında bir method oluşturdum.
Bu methodda önce liskedlist'in dolu olup olmadığını kontrol ettim. Ardından linkedlist'in uzunluğunun tek sayı veya çift sayı olduğunu kontrol ettim.
Bu işleme göre linkedlist'in ortasındaki elemanın bir adet mi yoksa iki adet mi olduğunu anladım. Daha sonra farklı bir linkedlist oluşturdum.
Oluşturmuş olduğum bu linkedlist tamamen rastgele oluşturuldu. Rastgele bir linkedlist oluşturduktan sonra ilk linkedlist'e bazı değerler ekledim.
Son olarak da ilk linkedlist ve rastgele oluşturulmuş olan ikinci linkedlist içerisindeki ortanca elemenları bulup ekrana yazdırdım.
