#Generate random password
#password harus ada huruf besar,kecil, angka dan simbol

import random
import string
pl=int(input("Panjang Password : "))
u=string.ascii_uppercase
l=string.ascii_lowercase
d=string.digits
s=string.punctuation
p=random.choice(u)+random.choice(l)+random.choice(d)+random.choice(s)
for i in range (pl-4):
    p=p+random.choice(u+l+d+s)
print("Random Password : "+p)
l=list(p)
random.shuffle(l)
pwd=''.join(l)
print("Acak dari password yang telah ditunjukkan : "+pwd)

