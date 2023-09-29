import re

file = open("KEI.html","r",encoding = "latin1")
teks = file.read()
file.close()
string = []
string = re.findall(r'([\w+]+)</a></td>', teks)
print(string)
