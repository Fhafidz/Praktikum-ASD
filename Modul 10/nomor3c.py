##Nomer 3.c
import timeit
import matplotlib.pyplot as plt

print("Nomer 3.c")
def soal_tiga(n):
    test = 0
    for i in range(n):
        test = test+1
    for j in range(n):
        test = test - 1

def uji_soal_tiga(n):
    ls = []
    jangkauan = range(1, n+1)
    siap = "from __main__ import soal_tiga"
    for i in jangkauan:
        t = timeit.timeit("soal_tiga(" + str(i) + ")", setup=siap, number=1)
        ls.append(t)
    return ls

n = 10
LS = uji_soal_tiga(n)
plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()