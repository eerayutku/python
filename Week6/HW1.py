import random


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

    def do_cycle(self):
        rtnode = self._rootNode
        counter = 0
        while rtnode != None:
            prevNode = rtnode
            rtnode = rtnode.nextNode
            counter = counter + 1
        rnd = random.randint(0, counter)
        rtnode = self._rootNode
        for i in range(0, rnd):
            rtnode = rtnode.nextNode

        prevNode.nextNode = rtnode

    def contains_cycle(self):
        if self._rootNode == None:
            print("RootNode Boştur")
            return
        slowptr = self._rootNode
        fastptr = self._rootNode
        while fastptr != None:
            slowptr = slowptr.nextNode
            fastptr = slowptr.nextNode.nextNode
            if fastptr == None:
                return False
            if fastptr == slowptr:
                return True


if __name__ == "__main__":
    a = LinkedList()
    a.add(5)
    a.add(10)
    a.add(20)
    a.add(29)
    a.dump()
    print("--" * 10)
    a.delete(20)
    a.dump()
    print("--" * 10)
    a.do_cycle()
    print(a.contains_cycle())