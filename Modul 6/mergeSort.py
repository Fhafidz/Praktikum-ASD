def mergeSort(A):
    print("Membelah", A)
    if len(A) > 1:
        mid = len(A) // 2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]
        
        mergeSort(separuhKiri)
        mergeSort(separuhKanan)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:
                A[k] = separuhKiri[i]
                i = i + 1
            else:
                A[k] = separuhKanan[j]
                j = j + 1
            k = k+1
            
            while i < len(separuhKiri):
                A[k] = separuhKiri[i]
                i = i+1
                k = k+1
                
            while j < len(separuhKanan):
                A[k] = separuhKanan[j]
                j = j+1
                k = k+1
    print('Menggabungkan', A)
 
arr = [80,7,24,16,43,91,35,2,19,72]  
mergeSort(arr)