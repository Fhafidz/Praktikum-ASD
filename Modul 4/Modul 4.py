'''
def cariLurus( wadah, target):
    n = len(wadah)
    for i in range (n):
        if wadah[i] == target:
            return True
    return False

A = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
print(cariLurus(A, 31))
print(cariLurus(A, 8))
'''

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

'''
target = 'Klaten'
for i in daftar:
    if i.kotaTinggal == target:
        print(i.nama + ' tinggal di ' + target)
 


def cariTerkecil(kumpulan):
    n = len(kumpulan)
    terkecil = kumpulan[0]
    for i in range(1,n):
        if kumpulan[i] < terkecil:
            terkecil = kumpulan[i]
    return terkecil



def binSe(kumpulan,target):
    low = 0
    high = len(kumpulan) - 1
    
    while low <= high:
        mid = (high + low) // 2
        if kumpulan[mid] == target:
            return True
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
B = [2,4,5,10,13,18,23,29,31,51,64]
print(binSe(B, 10))

#### Soal Nomor 1 ####
def pencarian(target):
    count = 0
    blank_List = []
    
    for i in daftar:
        if i.kotaTinggal == target:
            blank_List.append(count)
        count += 1
    
    if len(blank_List):
        print(blank_List)
    else:
        print('Tidak ditemukan')
   
print(pencarian('Klaten'))


#### Soal Nomor 2 ####
def uangTerkecil(data):
    
    terkecil = data[0]
    
    for i in range(len(data)):
        if data[i].UangSaku < terkecil.UangSaku:
            terkecil = data[i]
            s = terkecil.UangSaku
    return s

print(uangTerkecil(daftar))     


#### Soal Nomor 3 ####
def uangTerkecil(data):
    terkecil = data[0]
    blank_List = []
    for i in range(len(data)):
        if data[i].UangSaku < terkecil.UangSaku:
            terkecil = data[i]
            blank_List.append(data[i])
        elif data[i].UangSaku == terkecil.UangSaku and data[i] not in blank_List and i!=0:
            blank_List.append(data[i])
    for i in blank_List:
        print(str(i.nama)+" uang saku "+str(i.UangSaku))
    return 
print(uangTerkecil(daftar))


#### Soal Nomor 4 ####
def kembali_uangSaku(data):
    blank_List = []
    for i in range(len(data)):
        if data[i].UangSaku < 250000:
            blank_List.append(data[i])
        elif data[i].UangSaku == 250000 and data[i] not in blank_List and i!=0:
            blank_List.append(data[i])
    for i in blank_List:
        print(str(i.nama)+" uang saku "+str(i.UangSaku))
    return 

print(kembali_uangSaku(daftar))


#### Soal Nomor 5 ####
class node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
def cari(head, cari):
    
    curr = head
    
    while curr != None:
        if curr.data == cari:
            return True
        curr = curr.next
    return False


a = node(2)
b = node (1)
c = node (5)
d = node(19)

a.next = b
b.next = c
c.next = d

print(cari(a, 5))


#### Soal Nomor 6 ####
def binSe(kumpulan,target):
    low = 0
    high = len(kumpulan) - 1
    
    while low <= high:
        mid = (high + low) // 2
        if kumpulan[mid] == target:
            return mid
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
    
B = [2,4,5,10,13,18,23,29,31,51,64]
print(binSe(B, 10))  
'''

#### Soal Nomor 7 ####
def binSe(kumpulan, target):
  low = 0
  high = len(kumpulan) - 1
  blank_List = []

  while low <= high:
    mid = (high + low) // 2
    if kumpulan[mid] == target:
      break
      
    elif target < kumpulan[mid]:
      high = mid - 1
    else:
      low = mid + 1
      
  for i in range(low, high):
    if kumpulan[i] == target:
      blank_List.append(i)
  return blank_List

B = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
print(binSe(B, 6))     

#### Soal Nomor 8 ####
def binSearching(kumpulan, target):
    
    low = 0
    high = len(kumpulan) -1

    while low <= high:
        mid = (high + low) //2
        if kumpulan[mid] == target:
            return mid
        elif kumpulan[mid] < target:
            high = mid +1
        else :
            low = mid -1
            
    return -1

b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

"""
untuk mencari berapa jumlah tebakan yang digunakan oleh Binary Search
yaitu dengan menggunakan Logaritma basis 2 (log2(n))
misalkan :
        // apabila terdapat elemen array berjumlah 100 maka memiliki maksimal 7 kali tebakan
           itu dikarenakan log2(100) = 6.643856189774725 sehingga diperoleh angka 7
           dapat juga diperoleh dari log2(128) = 7 karena yang mendekati dari 100 adalah 128
       //  apabila terdapat elemen array berjumlah 1000 maka memiliki maksimal 10 kali tebakan
           itu dikarenakan log2(1000) = 9.965784284662087 sehingga diperoleh angka 10
           dapat juga diperoleh dari log2(1024) = 10 karena yang mendekati dari 1000 adalah 128
"""