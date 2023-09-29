# Buatlah list kuadrat bilangan 0 sampai 6

sr = [x**2 for x in range (0,7)]

# Buatlah list yang berisi tuple pasangan bilangan dengan kuadrat bilangan 0 sampai 6

a = [[x,x**2] for x in range (0,7)]

# Buatlah list kuadrat bilangan genap antara 0 sampai 15

b = [x**2 for x in range (0,15) if x%2 == 0]

# Buatlah list sepanjang 5 elemen yang berisi bilangan 3

c = [3 for j in range(5)]

# Buatlah list sepanjang 3 elemen yang berisi list sepanjang 3 elemen angka 0

d = [[0 for j in range (3)] for i in range (3)]

# Buatlah matrix identitas 3x3

e = [[1 if j==i else 0 for j in range (3)] for i in range (3)]

# Bilangan prima
def apakahPrima(x):
    for i in range (2,x):
        if x % i != 0:
            continue
    
f = [x for x in range (20,50) if apakahPrima(x)]


# Node
'''
class node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
def kunjungi(head):
    curNode = head
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next

a = node(11)
b = node(52)
c = node(18)
d = node(5)
e = node(67)

d.next = a
a.next = b
b.next = c
c.next = e
'''
# Node lanjutan

a = node(11)
b = node(52)
c = node(18)
d = node(5)
e = node(67)

class node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def kunjungi(head):
        cons = head
        while cons is not None:
            print(cons.data)
            cons = cons.next

    def cari(head, cari):
        cons = head
        while cons is not None:
            if cons == cari:
                print("data ditemukan")
            else:
                print("data tidak ditemukan")
            cons = cons.next
    
    def tambahDepan(head):
        Newnode = node(head)
        Newnode.next = a
        return Newnode
    
    def tambahAkhir(head):
        Newnode = node(head)
        e.next = Newnode
        return e
    
    def tambah(head, posisi):
        Newnode = node(head)
        Newnode.next = posisi.next
        posisi.next = Newnode.next
        head.head = posisi
        return head
        
            

    