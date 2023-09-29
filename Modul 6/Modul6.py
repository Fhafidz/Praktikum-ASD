def gabungkanDuaListUrut(a,b):
    blank_list = []
    c = a + b
    for i in c:
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
    print("Sesudah pengurutan : ",blank_list)
     

p = [2,8,15,23,37]
q = [4,6,15,20]
print(gabungkanDuaListUrut(p,q))