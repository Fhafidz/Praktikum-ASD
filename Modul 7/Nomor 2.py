import re

file = open("Indonesia.txt","r", encoding = "utf-8")
teks = file.read()
file.close()
string = []
string = re.findall(r"di\w+", teks)
print(string)