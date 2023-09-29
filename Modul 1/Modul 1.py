'''
### Nomor 1 ###


def cetakSiku(x):
    for i in range (x):
        for r in range (i+1):
            print("*", end='')
        print('')
        
a = int(input("Masukkan nilai : "))
cetakSiku(a)


### Nomor 2 ###


def gambarlahPersegiEmpat(a,b):
   for i in range (a):
        for r in range (b):
            if i == 0 or i == a-1 or r == 0 or r == b-1:
              print("@", end='')
            else:
                print(" ",end="")
        print()

gambarlahPersegiEmpat(4,5)


### Nomor 3A ###


def hurufVokal(a):
    
    vokal = ['a','i','u','e','o']
    jml_huruf = 0
    jml_vokal = 0
    
    for i in a:
        jml_huruf += 1
        if i in vokal:
            jml_vokal += 1
            
    x = (jml_huruf,jml_vokal)        
    print(x)

a = input('Masukkan kata : ')
hurufVokal(a)     


### Nomor 3B ###


def hurufKonsonan(a):
    
    vokal = ['a','i','u','e','o']
    jml_huruf = 0
    jml_vokal = 0
    
    for i in a:
        jml_huruf += 1
        if i in vokal:
            jml_vokal += 1
            
    jml_konsonan = jml_huruf-jml_vokal        
    x = (jml_huruf,jml_konsonan)        
    print(x)

a = input('Masukkan kata : ')
hurufKonsonan(a) 


### Nomor 4 ###


def rerata(b):
    x = sum (b) / len (b)
    print(x)
    
rerata([1,2,3,4,5])
g = [3,4,5,4,3,4,5,2,2,10,11,23]
rerata(g)


### Nomor 5 ###


from math import sqrt as sq

def apakahPrima(n):
    n = int(n)
    assert n >= 0
    primaKecil = [2, 3, 5, 7, 11]
    bukanPrKecil = [0, 1, 4, 6, 8, 9, 10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2, int(sq(n)) + 1):
            if n % i == 0:
                print ('False')
        print ('True')
            
apakahPrima(17)
apakahPrima(97)
apakahPrima(123)

        
### Nomor 6 ###


from math import sqrt as sq
def angkaPrima(a):
    if a < 2:
        return False
    for i in range(2,int(sq(a))+1):
        if a % i == 0:
            return False
    return True

for i in range(2,1001):
    if angkaPrima(i):
        print(i)
 
 
### Nomor 7 ###

 
def faktorisasiPrima(n):
    faktor = []
    i = 2
    while i <= n:
        if n % i == 0:
            faktor.append(i)
            n = n / i
        else:
            i += 1
    return faktor

n = int(input("Masukkan bilangan bulat positif: "))
faktor_prima = faktorisasiPrima(n)
print("Faktorisasi prima dari", n, "adalah:", faktor_prima)


### Nomor 8 ###


def apakahTerkandung(a,b):
    if a in b:
        print('true')
    else:
        print('false')

a = input('Masukkan kata a : ')
b = input('Masukkan kata b : ')
apakahTerkandung(a,b)


### Nomor 9 ###


for i in range (1,100):
    if i % 3 == 0 and i % 5 == 0:
        print('Python UMS')
    elif (i % 3) == 0:
        print('Python')
    elif (i % 5) == 0:
        print('UMS')
    else:
        print(i)

        
### Nomor 10 ###


from math import sqrt as sq
def selesaikanABC(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    d = (b**2) - (4*a*c)
    if (d < 0):
        print("Determinan negatif. Persamaan tidak mempunyai akar real.")
    else:
        x1 = (-b + sq(d))/(2*a)
        x2 = (-b - sq(d))/(2*a)
        hasil = (x1,x2)
        print(hasil)
    
selesaikanABC(1,2,3)

    
### Nomor 11 ###


def apakahKabisat(a):
    if (a % 4) == 0:
        if (a % 100) == 0:
            if (a % 400) == 0:
                print('true')
            else:
                print('false')
        else:
            print('true')
    else:
        print('false')

apakahKabisat(2400)
 
        
### Nomor 12 ###


import random

a = random.randint(1,100)
b = int(input('Tebak angka : '))
print('Permainan tebak angka.'+'\n'+'Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak')

for i in range(1,100):
    if i == a:
        print('angka random : ', i)
        if i == b:
            print('tebakan anda benar')
        elif i > b:
            print('angka', b ,'terlalu kecil, silahkan coba lagi')
        else:
            print('angka', b ,'terlalu besar, silahkan coba lagi')
'''

### Nomor 13 ###


angka = {1:"satu " , 2:"dua " , 3:"tiga " , 4:"empat " , 5:"lima " , 6:"enam " , 7:"tujuh " , 8:"delapan " , 9:"sembilan "}

b = "puluh "
c = "ratus "
d = "ribu "
e = "juta "
f = "milyar "
g = "triliun "

def katakan(x):
    y = str(x)
    n = len(y)
    if n <= 3:
        if n == 1:
            if y == "0":
                print ("")
            else:
                print (angka[int(y)])
        elif n == 2:
            if y[0] == "1":
                if y[1] == "1":
                    print ("sebelas")
                elif y[0] == "0":
                    x = y[1]
                    print (katakan(x))
                elif y[1] == "0":
                    print ("sepuluh")
                else:
                    print (angka[int(y[1])] + "belas")
            elif y[0] == "0":
                x = y[1]
                print (katakan(x))
            else:
                x = y[1]
                print (angka[int(y[0])] + b + katakan(x))
        else:
            if y[0] == "1":
                x = y[1:]
                print ("seratus " + katakan(x))
            elif y[0] == "0":
                x = y[1:]
                print (katakan(x))
            else:
                x = y[1:]
                print (angka[int(y[0])] + c + katakan(x))
    elif 3 < n <= 6:
        p = y[-3:]
        q = y[:-3]
        if q == "1":
            print  ("seribu " + katakan(p))
        elif q == "000":
            return katakan(p)
        else:
            print (katakan(q) + d + katakan(p))
    elif 6 < n <=9:
        r = y[-6:]
        s = y[:-6]
        print (katakan(s) + e + katakan(r))
    elif 9 < n <=12:
        t = y[-9:]
        u = y[:-9]
        print (katakan(u) + f + katakan(t))
    else:
        v = y[-12:]
        w = y[:-12]
        print (katakan(w) + g + katakan(v))


### Nomor 14 ###

'''
def formatRupiah(a):
    rupiah = "Rp {:,.0f}".format(a)
    print(rupiah)

formatRupiah(1500)
formatRupiah(2560000)
'''