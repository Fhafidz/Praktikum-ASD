### NOMOR 1 ###
    
class Pesan(object):
    
    def __init__ (self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks) 
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))      
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))        
    def jumKar(self):
        return len(sel.teks)    
    def cetakJumlahKarakterku(self):
        print('kalimatku mempunyai', len(self.teks),'karakter')        
    def perbarui(self,stringBaru):
        self.teks = stringBaru        
    def apakahTerkandug(self,kata):
        if kata in self.teks:
            return True
        else:
            return False
        
    def hitungKonsonan(self):
        vokal = ['a','i','u','e','o','A','I','U','E','O']
        jml_Konsonan = 0
        for i in self.teks:
            if i not in vokal and i != '':
                jml_Konsonan += 1
        return jml_Konsonan
    
    def hitungVokal(self):
        vokal = ['a','i','u','e','o','A','I','U','E','O']
        jml_Vokal = 0
        for i in self.teks:
            if i in vokal and i != '':
                jml_Vokal += 1
        return jml_Vokal


###  NOMOR 2,3,4,5 ###

class Manusia(object):
    keadaan = 'lapar'
    def __init__(self,nama):
        self.nama = nama        
    def ucapkanSalam(self):
        print("Salam Namaku", self.nama)        
    def makan(self,s):
        print("Saya baru saja makan",s)
        self.keadaan = 'kenyang'        
    def olahraga(self,k):
        print("Saya baru saja latihan",k)
        self.keadaan = 'lapar'        
    def mengalikanDenganDua(self,n):
        return n*2

class Mahasiswa(Manusia):
    def __init__(self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ',NIM' + str(self.NIM) \
            + '.Tinggal di' + self.kotaTinggal \
            + '.Uang saku' + str(self.uangSaku) \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama   
    def ambilNIM(self):
        return self.NIM   
    def ambilUang(self):
        return self.uangSaku  
    def makan(self,s):
        print("Saya baru saja makan",s,"sambil belajar")
        self.keadaan = 'kenyang'       
    def ambilKota(self):
        return self.kotaTinggal
    def perbaruiKota(self,k):
        self.kotaTinggal = k
        return self.kotaTinggal
    def tambahUang(self,u):
        u = int(u)
        jumlah = self.uangSaku + u
        self.uangSaku = jumlah
        return self.uangSaku

    listKuliah = []
    def ambilkuliah(self,m):
        self.listKuliah.append(m)      
    def hapusKuliah(self,x):
        self.listKuliah.remove(x)

m1 = Mahasiswa('Fariz',100,'Pati',10000)
m2 = Mahasiswa('Taufiqul',101,'Semarang',20000)
m3 = Mahasiswa('Hafidz',102,'Kudus',30000)
        


###  NOMOR 6 ###

class siswaSMA(Manusia):
    
    def __init__(self,nama,no_induk,kelas,alamat):
        self.nama = nama
        self.nomor = no_induk
        self.kelas = kelas
        self.alamat = alamat
        
    def __str__(self):
        a = "Nama : "+self.nama \
            +"No Induk : "+str(self.no) \
            +"Tinggal di : "+self.alamat \
            +"Kelas : "+str(self.kelas)
        return a
    
    def ambilNama(self):
        return self.nama
    
    def ambilNoInduk(self):
        return self.nomor
    
    def ambilKelas(self):
        return self.kelas
    
    def ambilAlamat(self):
        return self.alamat

    
s1 = siswaSMA('Hafidz',205,'XII','Kudus')


###  NOMOR 7 ###

class MhsTIF(Mahasiswa):
    
    def katakanPy(self):
        print('Python is cool.')
        

