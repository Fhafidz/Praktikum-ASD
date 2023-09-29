from timeit import timeit

def jumlahkan_cara_1(n):
    hasilnya = 0
    for i in range(1, n+1):
        hasilnya = hasilnya + i
    return hasilnya

def jumlahkan_cara_2(n):
    return (n * (n + 1)) / 2

def insertionsort(a):
    for i in range(1, len(a)):
        nilai = a[i]
        b = i
        while b > 0 and nilai < a[b - 1]:
            a[b] = a[b - 1]
            b -= 1
        a[b] = nilai

n = 10000
waktu_jml_cara_1 = timeit(lambda: jumlahkan_cara_1(n), number=1)
print("Waktu Jumlahkan Cara 1:", waktu_jml_cara_1)

n = 10000
waktu_jml_cara_2 = timeit(lambda: jumlahkan_cara_2(n), number=1)
print("Waktu Jumlahkan Cara 2:", waktu_jml_cara_2)

a = list(range(10000))
waktu_insertion_sort = timeit(lambda: insertionsort(a), number=1)
print("Waktu insertionSort:", waktu_insertion_sort)
