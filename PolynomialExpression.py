#singly-LinkedList 
#สมการพหุนามตัวแปรเดียว
class Node: #ให้แต่ละ Node แทนแต่ละพจน์ใน polynomial
    def __init__(self,coef,expo,next = None):
        self.coef = coef #สัมประสิทธิ์
        self.expo = expo #เลขชี้กำลัง
        self.next = next

class LinkList: #แทนสมการ polynomial 1 สมการ
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def isEmpty(self):
        return self.head == None
    
    def append(self,coef,expo):
        p = Node(coef,expo)
        if self.isEmpty():
            self.head = self.tail = p
        else :
            t = self.head
            self.tail.next = p
            self.tail = p
        self.size += 1

    def __str__(self):
        if not self.isEmpty():
            t = self.head
            s = ''
            while t.next != None:
                if(t.expo > 1):
                    s += str(t.coef) + 'x^' + str(t.expo) + ' + '
                elif t.expo == 1 :
                    s += str(t.coef) + 'x + '
                else :
                    s += str(t.coef) + ' + '
                t = t.next
            if(t.expo > 1):
                return s + str(t.coef) + 'x^' + str(t.expo)
            elif t.expo == 1 :
                return s + str(t.coef) + 'x'
            else :
                return s + str(t.coef)
        else :
            return 'None'
    
    def addPolynomial(self,head):
        if self.head == None:
            self.head = head
        else :
            while head != None:
                state = 0
                t = self.head
                while t != None:
                    if t.expo == head.expo :
                        t.coef += head.coef
                        state = 1
                        break
                    else :
                        t = t.next
                if state != 1 :
                    p = head
                    head = head.next
                    t = self.head
                    if p.expo > self.head.expo:
                        p.next = self.head
                        self.head = p
                    else :
                        while t.next != None:
                            if p.expo < t.expo:
                                p.next = t.next
                                t.next = p
                            t = t.next
                head = head.next
                    

P = input("Enter P(x) : ").split(' + ') #coefficent 0 < x < 9 , exponect 0 < n < 9
Q = input("Enter Q(x) : ").split(' + ') #coefficent 0 < x < 9 , exponect 0 < n < 9
Lp = LinkList()
Lq = LinkList()
for item in P:
    if item.isnumeric():
        Lp.append(int(item),0)
    else :
        if item[-1].isnumeric():
            n = item.split('x^')
            Lp.append(int(n[0]),int(n[1]))
        else :
            n = item[:-1]
            Lp.append(int(n),1)
for item in Q:
    if item.isnumeric():
        Lq.append(int(item),0)
    else :
        if item[-1].isnumeric():
            n = item.split('x^')
            Lq.append(int(n[0]),int(n[1]))
        else :
            n = item[:-1]
            Lq.append(int(n),1)
            
print(Lp)
print(Lq)
Lp.addPolynomial(Lq.head)

print('P(x) + Q(x) = ' + Lp.__str__())

