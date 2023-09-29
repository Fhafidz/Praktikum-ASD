class _SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None
    
# Fungsi menampilakan informasi level
def info(akar, count = 0):
    if akar is not None:
        print (akar.data + ',level ' + str(count))
        (info(akar.kiri, count +1), info(akar.kanan, count +1))    
        
# Membuat simpul-simpul dan mengisi data
A = _SimpulPohonBiner('Ambarawa')
B = _SimpulPohonBiner('Bantul')
C = _SimpulPohonBiner('Cimahi')
D = _SimpulPohonBiner('Denpasar')
E = _SimpulPohonBiner('Enrekang')
F = _SimpulPohonBiner('Flores')
G = _SimpulPohonBiner('Garut')
H = _SimpulPohonBiner('Halmahera Timur')
I = _SimpulPohonBiner('Indramayu')
J = _SimpulPohonBiner('Jakarta')

# Menghubungkan simpul ortu-anak
A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; C.kanan = G
E.kiri = H
G.kanan = I

#Eksekusi Program
info(A)