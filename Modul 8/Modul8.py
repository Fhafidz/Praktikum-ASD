class Stack(object):
    def __init__(self): # Membuat stack kosong.
        self.items = [] # List untuk menyimpan stack.
    
    def isEmpty(self): # Mengembalikan True kalau kosong,
        return len(self)==0 # selain itu False
    
    def __len__(self): # Mengembalikan banyaknya item di stack.
        return len(self.items) #
    
    def peek(self): # Mengembalikan nilai posisi atas tanpa menghapus.
        assert not self.isEmpty(), "Stack kosong. Tidak bisa diintip"
        return self.items[-1]
    
    def pop(self): # Mengembalikan nilai posisi atas lalu menghapus.
        assert not self.isEmpty(), "Stack kosong. Tidak bisa di-pop"
        return self.items.pop()
    
    def push(self, data): # Mendorong item baru ke stack.
        self.items.append(data)

class StackLL(object):
    def __init__(self):
        self.top = None
        self.size = 0
        
    def isEmpty(self):
        return self.top is None
    
    def __len__(self):
        return self.size
    
    def peek(self):
        assert not self.isEmpty(), "Tidak bisa diintip. Stack kosong."
        return self.top.item
    
    def pop(self):
        assert not self.isEmpty(), "Tidak bisa pop dari stack kosong."
        node = self.top
        self.top = self.top.next
        self.size -= 1
        return node.item
    
    def push(self, data):
        self.top = _StackNode(data, self.top)
        self.size += 1
        
class _StackNode(object):
    def __init__(self, data, link):
        self.item = data
        self.next = link
        

'''''       
PROMPT = "Masukkan bilangan positif (<0 untuk mengakhiri):"
myStack = Stack()
value = int(input( PROMPT ))
while value >= 0:
    myStack.push(value)
    value = int(input( PROMPT ))
while not myStack.isEmpty():
    value = myStack.pop()
    print(value)


def cetakBiner(d):
    f = StackLL()
    if d==0: f.push(0);
    while d != 0:
        sisa = d%2
        d = d//2
        f.push(sisa)
    st = ''
    for i in range (len(f)):
        st = st + str (f.pop())
    return st


# Nomer 1
def cetakHexa(d):
    f = StackLL()
    if d==0: f.push(0);
    while d!=0:
        sisa = d%16
        d = d//16
        f.push(sisa)    
    x = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']  
    st = ''
    for i in range (len(f)):
        st = st + str (x[f.pop()])
    return st

print(cetakHexa(12))
print(cetakHexa(31))
print(cetakHexa(229))
print(cetakHexa(255))
print(cetakHexa(31519))
'''

# Nomer 2
nilai = Stack()         #Membuat objek dari kelas stack
for i in range(16):     #Untuk i di dalam range 16
    if i % 3 == 0:      #Jika sisa bagi i dengan 3 sama dengan 0
        nilai.push(i)   #Memasukkan i kedalam nilai stack
                        #Output 15,12,9,6,3,0
     

# Nomer 3
nilai = Stack()         #Membuat objek dari kelas stack
for i in range(16):     #untuk i di dalam range 16
    if i % 3 == 0:      #Jika sisa bagi i dengan 3 sama dengan 0
        nilai.push(i)   #Memasukkan i kedalam nilai stack
    elif i % 4 == 0:    #tetapi Jika sisa bagi i dengan 4 sama dengan 0
        nilai.pop()     #Mengembalikan nilai dari item paling atas 
                        #pada nilai stack lalu menghapusnya
                        #Output 15,12,9,0




#nomer 4
class Queue():
    def __init__(self):
        self.qlist = []
    def is_empty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist.pop(0)
    def get_front_most(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[0]
    def get_rear_most(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[-1]

Y = Queue()
Y.enqueue(30)
Y.enqueue(26)
Y.enqueue(7)
Y.enqueue(18)
Y.enqueue(14)

print(Y.get_front_most())
print(Y.get_rear_most())
print(Y.qlist)

#nomer 5
class PriorityQueue():
    def __init__(self):
        self.qlist = []
    def __len__(self):
        return len(self.qlist)
    def is_empty(self):
        return len(self) == 0
    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)
    def get_front_most(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[0]
    def get_rear_most(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[-1]
    def dequeue(self):
        A = []
        for i in self.qlist:
            A.append(i)
        s = 0
        for i in range(1, len(self.qlist)):
            if A[i].priority < A[s].priority:
                s = i
        hasil = self.qlist.pop(s)
        return hasil.item

class _PriorityQEntry():
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

f = PriorityQueue()
f.enqueue("Topi",3)
f.enqueue("Baju",5)
f.enqueue("Celana",1)
f.enqueue("Jas",2)
f.enqueue("Jaket",4)

print(f.dequeue())
print(f.dequeue())
print(f.dequeue())
print(f.dequeue())
print(f.dequeue())