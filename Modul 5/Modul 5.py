def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp
    
k = [50,20,70,10]
swap(k,1,3)
print(k)

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range (dariSini+1, sampaiSini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
        return posisiYangTerkecil
    
A = [18, 13, 44, 25, 66, 107, 78, 89]
j = cariPosisiYangTerkecil(A, 2, len(A))
print(j)

def bubbleSort(A):
    n = len(A)
    for i in range (n-1):
        for j in range (n-i-1):
            if A[j] > A[j+1]:
                swap(A, j, j+1)
                
def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i :
            swap(A, i, indexKecil)
            
def insertionSort(A):
    n = len(A)
    for i in range (1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = i
            pos = pos - 1
        A[pos] = nilai

class mhsTIF ():
    def __init__(self,x,y,z,v):
        self.nama = x
        self.umur = y
        self.kotaTinggal = z
        self.UangSaku = v

c0 = mhsTIF('Ika',10,'Sukoharjo',240000)
c1 = mhsTIF('Budi',51,'Sragen',230000)
c2 = mhsTIF('Ahmad',2,'Surakarta',250000)
c3 = mhsTIF('Chandra',18,'Surakarta',235000)
c4 = mhsTIF('Eka',4,'Boyolali',240000)
c5 = mhsTIF('Fandi',31,'Salatiga',250000)
c6 = mhsTIF('Deni',13,'Klaten',245000)
c7 = mhsTIF('Galuh',5,'Wonogiri',245000)
c8 = mhsTIF('Janto',23,'Klaten',245000)
c9 = mhsTIF('Hasan',64,'Karanganyar',270000)
c10 = mhsTIF('Khalid',29,'Purwodadi',265000)

daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

