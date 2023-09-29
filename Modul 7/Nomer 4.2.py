import re

file = open("KEI.html","r",encoding = "latin1")
teks = file.read()
file.close()
string = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>',teks)

list = []
for i in string:
    list.append((i[0], float(i[1])))
    
print(list)