##Nomer 3.f
import timeit
import matplotlib.pyplot as plt

print("Nomer 3.f")
def soal_tiga(n):
    for i in range(n):
        for j in range(i):
            for k in range(j):
                m = i + j + k + 2019

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