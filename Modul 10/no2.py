import time
import random

        
#Average Case Scenario
def averagecase():
    for i in range(5):
        L = list(range(90000))
        random.shuffle(L)
        awal = time.time()
        U = sorted(L)
        akhir = time.time()
        print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" % (len(L), akhir - awal))
        
#Worst Case Scenario
def worstcase():
    for i in range(5):
        L=list(range(90000))
        L=L[::-1]
        awal=time.time()
        U = sorted(L)
        akhir=time.time()
        print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" %(len(L), akhir - awal))
        
#Best Case Scenario
def bestcase():
    for i in range(5):
        L = list(range(90000))
        awal = time.time()
        U = sorted(L)
        akhir = time.time()
        print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" %(len(L), akhir - awal))
        


#Best Case Sorted g
print("=========== Waktu Bestcase Sorted  ===========")
bestcase()

#Average Case Sorted g
print("=========== Waktu Average Sorted  ===========")
averagecase()

#Worst Case Sorted g
print("=========== Worst Average Sorted  ===========")
worstcase()
