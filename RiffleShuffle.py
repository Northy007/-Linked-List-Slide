# Input LinkedList(L1) , LinkedList(L2) : 4 5 6,1 2 3 7 8
# 4 -> 5 -> 6
# 1 -> 2 -> 3 -> 7 -> 8
# Riffle Shuffle : 4 -> 1 -> 5 -> 2 -> 6 -> 3 -> 7 -> 8

#singly-linkedlist
class Node :
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        if not self.isEmpty():
            t = self.head
            s = ''
            while t.next != None:
                s += str(t.data) + ' -> '
                t = t.next
            return s + str(t.data)
        else :
            return 'None'

    def append(self,data):
        p = Node(data)
        if self.isEmpty():
            self.head = self.tail = p
        else :
            self.tail.next = p
            self.tail = p
        self.size += 1

    def riffle(self,link):
        linkSize = link.size
        self.size += linkSize
        if self.isEmpty() and not link.isEmpty():
            self.head = link.head
        elif not link.isEmpty() :
            t = self.head
            p = link.head
            while t.next != None:
                link.head = link.head.next
                p.next = t.next
                t.next = p
                t = t.next.next
                p = link.head
                linkSize -= 1
                if p == None :
                    break
            self.tail.next = link.head
            if linkSize != 0:
                self.tail = link.tail
        else :
            pass
            

inp = input("Input LinkedList(L1) , LinkedList(L2) : ").split(',')
lst1 = inp[0].split(' ')
lst2 = inp[1].split(' ')
L1 = LinkedList()
L2 = LinkedList()
for item in lst1 :
    L1.append(item) 
for item in lst2 :
    L2.append(item) 
print(L1)
print(L2)
L1.riffle(L2)
print("Riffle Shuffle : " + L1.__str__())



