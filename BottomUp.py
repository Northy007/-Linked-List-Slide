
#singly-LinkedList
class Node:
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

    def append(self,data):
        p = Node(data)
        if self.isEmpty():
            self.head = self.tail = p
        else :
            self.tail.next = p
            self.tail = p
        self.size += 1

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

    def bottomUp(self,percent):
        index = int(self.size*(percent/100))
        t = self.head #t คือ head ของ linkedlist
        for i in range(index - 1):
            t = t.next #t คือตัวที่จะตัดหรือตัวที่จะกลายเป็น tail สมมจว่าเป็น e1 ** t = e1
        #ให้ตัวถัดไปของ tail ปัจจุบัน กลายเป็น head
        self.tail.next = self.head  
        #head -> e1 -> e2 -> e3 -> tail -> None กลายเป็น head -> e1 -> e2 -> e3 -> tail -> head -> e1 -> ... ซึ่งแบบนี้มันจะเป็น infinity loop
        
        #ให้ head คือตัวถัดไปของ t หรือก็คือ e2
        self.head = t.next
        #e0 -> e1 -> head -> e3 -> tail -> e0 -> e1 -> .....

        #ให้ tail คือ t หรือก็คือ e1 เพื่อให้มันเป็นตัวท้าย
        self.tail = t
        #head -> e3 -> e4 -> e0 -> tail -> head -> e3 -> e4 -> e0 -> tail -> ...

        #ให้ตัวถัดไปของ tail เป็น None จะได้ไม่เป็น infinity loop
        self.tail.next = None
        #head -> e3 -> e4 -> e0 -> tail -> None
        # e2  -> e3 -> e4 -> e0 ->  e1  -> None

inp = input("Input elements, Lift(Percent): ").split(',')
list = inp[0].split(' ')
print(list)
percent = float(inp[1][:-1])
L = LinkedList()
for item in list:
    L.append(item)
print('start : ' + L.__str__())
L.bottomUp(percent)
print('bottomUp : ' + L.__str__())

