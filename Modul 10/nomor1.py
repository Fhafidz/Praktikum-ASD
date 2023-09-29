from timeit import timeit

# Jumlah Cara 1
def jumlahkan_cara_1(n):
    hasilnya = 0
    for i in range(1, n+1):
        hasilnya = hasilnya + i
    return hasilnya

# Jumlah Cara 2
def jumlahkan_cara_2(n):
    return (n*(n+1))/2

# Insertion Sort
def insertionsort(a):
    for i in range(1, len(a)):
        nilai = a[i]
        b = i
        while b > 0 and nilai < a[b - 1]:
            a[b] = a[b-1]
            b -= 1
        a[b] = nilai
        
x = 10
y = [5,1,9,6,2,4,8.3,7,0]

def jml1():
    jumlahkan_cara_1(x)
    
def jml2():
    jumlahkan_cara_2(x)
    
def inst():
    insertionsort(y)

if __name__ == '__main__':
    import timeit
    
    print("Jumlahkan cara 1 timeit")
    print(timeit.timeit("jml1()", setup="from __main__ import jml1"))
    
    print("\nJumlahkan cara 2 timeit")
    print(timeit.timeit("jml2()", setup="from __main__ import jml2"))
    
    print("\nInsertionSort timeit")
    print(timeit.timeit("inst()", setup="from __main__ import inst"))
