class mhsTIF ():
    def __init__(self,x,y,z,v):
        self.nama = x
        self.nim = y
        self.kotaTinggal = z
        self.UangSaku = v

c0 = mhsTIF('Ika',102,'Sukoharjo',240000)
c1 = mhsTIF('Budi',104,'Sragen',230000)
c2 = mhsTIF('Ahmad',101,'Surakarta',250000)
c3 = mhsTIF('Chandra',107,'Surakarta',235000)
c4 = mhsTIF('Eka',105,'Boyolali',240000)
c5 = mhsTIF('Fandi',109,'Salatiga',250000)
c6 = mhsTIF('Deni',106,'Klaten',245000)
c7 = mhsTIF('Galuh',108,'Wonogiri',245000)
c8 = mhsTIF('Janto',103,'Klaten',245000)
c9 = mhsTIF('Hasan',120,'Karanganyar',270000)
c10 = mhsTIF('Khalid',114,'Purwodadi',265000)

daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def swap(a,p,q):
    tmp = a[p]
    a[p]=a[q]
    a[q]=tmp
    
def bubbleSort(a):
    blank_list = []
    for i in a:
        blank_list.append(i.nim)
    print("Sebelum pengurutan : ",blank_list)
    
    n = len(blank_list)
    for i in range(n):
        for j in range(n-i-1):
            if blank_list[j] > blank_list[j+1]:
                swap(blank_list,j,j+1)
    return blank_list
    
   
print("Setelah pengurutan : ",bubbleSort(daftar))