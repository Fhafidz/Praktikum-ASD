import time
import random

RUN = 32
def insertionSort(arr, left, right):
    for i in range(left + 1, right+1):
        temp = arr[i]
        j = i - 1
        while j >= left and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
        
#MergeSorted
def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
    i, j, k = 0, 0, l
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

#timeSort
def timSort(arr, n):
    for i in range(0, n, RUN):
        insertionSort(arr, i, min((i+31), (n-1)))
    size = RUN
    while size < n:
        for left in range(0, n, 2*size):
            mid = left + size - 1
            right = min((left + 2*size - 1), (n-1))
            merge(arr, left, mid, right)
        size = 2*size
        
g = [5, 21, 7, 23, 19]
n = len(g)
print("g = ", g)
z = [5, 21, 7, 23, 19]
print("z = ", z)
a = [9, 5, 4, 6, 8, 1, 2]
print("a=", a)

#timSort
timSort(g, len(g))
print("=========================timsort========================")
print("g = ", g)

#a.sort()
print("=========================a.sort()=======================")
a.sort()
print("a=", a)

#Sorted
z = [5, 21, 7, 23, 19]
print("=========================sorted=========================")
sorted(z)
print("z = ", z)

#bestcaseSorted
print("=======================Best Case Sorted===================")

def bestcase():
    for i in range(5):
        L = list(range(3000))
        awal = time.time()
        U = sorted(L)
        akhir = time.time()
        print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" %(len(L), akhir - awal))
bestcase()

#AverageCase
print("======================Average Case Sorted==================")
def averagecase():
    for i in range(5):
        L = list(range(3000))
        random.shuffle(L)
        awal = time.time()
        U = sorted(L)
        akhir = time.time()
        print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" % (len(L), akhir - awal))
averagecase()

#worstCase
print("======================Worst Case Sorted====================")
def worstcase():
    for i in range(5):
        L=list(range(3000))
        L=L[::-1]
        awal=time.time()
        U=sorted(L)
        akhir=time.time()
        print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" %(len(L), akhir - awal))
worstcase()
