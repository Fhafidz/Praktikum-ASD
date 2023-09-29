a = [1,3,5,7,9]
b = [2,4,6,8,10]

def insertionSort(x,y):
    blank_list = []
    x.extend(y)
    for i in x:
        blank_list.append(i)
    print("Sebelum pengurutan : ",blank_list)
    
    n = len(blank_list)
    for i in range (1,n):
        nilai = blank_list[i]
        pos = i
        while pos > 0 and nilai < blank_list[pos-1]:
            blank_list[pos] = blank_list[pos-1]
            pos = pos-1
        blank_list[pos] = nilai
    return blank_list
      
        
print("Setelah pengurutan : ",insertionSort(a,b))
