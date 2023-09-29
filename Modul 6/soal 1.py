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

daftar = [c0.nim, c1.nim, c2.nim, c3.nim, c4.nim, c5.nim, c6.nim, c7.nim, c8.nim, c9.nim, c10.nim]

def mergeSort(A):
    print("Membelah", A)
    if len(A) > 1:
        mid = len(A) // 2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]
        
        mergeSort(separuhKiri)
        mergeSort(separuhKanan)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:
                A[k] = separuhKiri[i]
                i = i + 1
            else:
                A[k] = separuhKanan[j]
                j = j + 1
            k = k+1
            
            while i < len(separuhKiri):
                A[k] = separuhKiri[i]
                i = i+1
                k = k+1
                
            while j < len(separuhKanan):
                A[k] = separuhKanan[j]
                j = j+1
                k = k+1
    print('Menggabungkan', A)
    
    
def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1 )
    
def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1) 
        quickSortBantu(A, titikBelah + 1, akhir)
    
def partisi(A, awal, akhir):
    nilaiPivot = A[awal] 

    penandaKiri = awal + 1 
    penandaKanan = akhir 

    selesai = False
    while not selesai: 

        while penandaKiri <= penandaKanan and A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1 

        while A[penandaKanan] >= nilaiPivot and penandaKanan >= penandaKiri: 
            penandaKanan = penandaKanan - 1 

        if penandaKanan < penandaKiri:
            selesai = True 
        else:
            temp = A[penandaKiri] 
            A[penandaKiri] = A[penandaKanan] 
            A[penandaKanan] = temp 

    temp = A[awal] 
    A[awal] = A[penandaKanan] 
    A[penandaKanan] = temp
    
    return penandaKanan


## Memanggil fungsi mergeSort()
mergeSort(daftar)

## Memanggil fungsi quickSort()
quickSort(daftar)
print("\n"+"Hasil QuickSort")
print(daftar)
