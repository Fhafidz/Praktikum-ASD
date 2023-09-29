import re
s = 'sebuah contoh kata:teh!!'
cocok = re.findall(r'kata:\w\w\w', s)
if cocok:
    print('menemukan', cocok)
else:
    print('tidak menemukan')