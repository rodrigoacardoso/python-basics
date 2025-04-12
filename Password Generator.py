import random
import string
len = int(input("Insert the password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
i=0
password=""
while i<len:
    i=i+1
    password += "".join(random.choice(characters))
print ("Password: ",password)
