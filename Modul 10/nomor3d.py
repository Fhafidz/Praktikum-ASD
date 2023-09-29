##Nomer 3.d
import timeit
import matplotlib.pyplot as plt

print("Nomer 3.d")
def soal_tiga(n):
    i = n
    while i > 0:
        k = 2 + 2
        i = i // 2

def uji_soal_tiga(n):
    ls = []
    jangkauan = range(1, n+1)
    siap = "from __main__ import soal_tiga"
    for i in jangkauan:
        ##print('i = ',i)
        t = timeit.timeit("soal_tiga(" + str(i) + ")", setup=siap, number=1)
        ls.append(t)
    return ls

n = 1000
LS = uji_soal_tiga(n)
plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()