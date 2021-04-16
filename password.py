# Base file

import random

length = int(input("Length of password: "))


temp = ""
for i in range(length):
    temp = temp + chr(random.randint(32,126))
print(temp)