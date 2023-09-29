a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
c = [[12,3,"x","y"],[12,33,4]]

def cek_Konsisten(n):
    column = set(len(i) for i in n)
    row = len(n)
    
    if len(column) == 1 and column.pop() == row:
        print("Matriks Konsisten")
    else:
        print("Matriks Tidak Konsisten")     
                            
                            
def get_Size(n):
    print("Matriks ini memiliki ukuran : " + str(len(n)) + "x" + str(len(n[0])))
 


def sum_Matrix(n,m):
    z = 0
    v = 0
    
    for i in n:
        for j in i:
            z+=1
            
    for i in m:
        for j in i:
            v+=1
        
    if z == v:
        n = [x for x in n]
        m = [y for y in m]
        x1 = n[0][0] + m[0][0]
        x2 = n[0][1] + m[0][1]
        y1 = n[1][0] + m[1][0]
        y2 = n[1][1] + m[1][1]
        result = [[x1,x2],[y1,y2]]
        print(result)
    else:
        print("Ukuran matriks tidak sama")


def kali_Matriks(n,m):
    z = 0
    v = 0
    
    for i in n:
        for j in i:
            z+=1
            
    for i in m:
        for j in i:
            v+=1
        
    if z == v:
        n = [x for x in n]
        m = [y for y in m]
        x1 = (n[0][0] * m[0][0]) + (n[0][1] * m[1][0])
        x2 = (n[0][0] * m[0][1]) + (n[0][1] * m[1][1])
        y1 = (n[1][0] * m[0][0]) + (n[1][1] * m[1][0])
        y2 = (n[1][0] * m[0][1]) + (n[1][1] * m[1][1])
        result = [[x1,x2],[y1,y2]]
        print(result)
    else:
        print("Ukuran matriks tidak sama")



def det_Matrix(n):
    if len(n) == len (n[0]):
        n = [x for x in n]
        det = (n[0][0]*n[1][1]) - (n[0][1]*n[1][0])
        print(det)
    else:
        print("Ukuran matriks tidak sama")








        
def buat_Nol(m, n=None):
    if n != None:
        matriks = [[0 for j in range (m)] for i in range(n)]
        print(matriks)
    else:
        matriks = [[0 for j in range (m)] for i in range(m)]
        print(matriks)   



def buat_Identitas(m):
    matriks = [[1 if j==i else 0 for j in range(m)] for i in range(m)]
    print(matriks)




class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def cetak(head):
        curr = head
        while curr != None:
            print(curr.data)
            curr = curr.nextNode

    def cari(head, cari):
        curr = head
        while curr != None:
            if curr.data == cari:
                print("Data ditemukan!")
            else:
                print("Check data!")
            curr = curr.nextNode

    def tambahDepan(head):
        newNode = Node(1)
        newNode.nextNode = head
        head = newNode
        return head

    def tambahAkhir(head):
        curr = head
        while curr is not None:
            if curr.nextNode == None:
                newNode = Node(25)
                curr.nextNode = newNode
                return curr
            else:
                pass
            curr = curr.nextNode
        return curr

    def tambah(head, posisi):
        newNode = Node(8)
        newNode.nextNode = posisi.nextNode
        posisi.nextNode = newNode
        head.head = posisi
        return head

    def hapus(head, posisi):
        curr = head
        while curr != None:
            if curr.nextNode.data == posisi:
                curr.nextNode = curr.nextNode.nextNode
                return curr
            else:
                pass
            curr = curr.nextNode
        return curr
'''  
a = Node(14)
b = Node(76)
c = Node(54)
d = Node(9796)

a.nextNode = b
b.nextNode = c
c.nextNode = d

# print(a.nextNode.nextNode.data)
a.tambah(b)
a.cari(14)
a.tambahAkhir()
a.tambahDepan()
a.cetak()   
'''            
      
   
   
            
class doubly_linked():
    def __init__(self, Data, Next=None, Prev=None):
        self.Data = Data
        self.Next = Next
        self.Prev = Prev

    def mencetak(head):
        curr = head
        while curr != None:
            print(curr.Data)
            if curr.Next == None:
                curr = curr
                break
            else:
                curr = curr.Next
        print("\n")
        while curr != None:
            print(curr.Data)
            curr = curr.Prev
            
    def simpulAwal(head):
        newNode = doubly_linked(25)
        newNode.Next = head
        head.Prev = newNode
        head =newNode
        return head





    def simpulAkhir(head):
        curr = head
        while curr != None:
            if curr.Next == None:
                newNode = doubly_linked(365)
                curr.Next = newNode
                newNode.Prev = curr
                return curr
            else:
                pass
            curr = curr.Next
        return curr        

hell = doubly_linked(14)
heaven = doubly_linked(15124)
between = doubly_linked(9999)

hell.Next = heaven
heaven.Next = between

hell.simpulAwal()
hell.simpulAkhir()
hell.mencetak()