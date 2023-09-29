import re

file = open("Indonesia.txt","r",encoding = "utf-8")
teks = file.read()
file.close()
string = []
string = re.findall(r"di\s\w+", teks)
print(string)