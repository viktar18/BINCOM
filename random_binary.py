import random

#generate a random 4 digits binary (string)
binary_digits = ""

for x in range(4):
    binary_digits += str(random.randint(0, 1))

print(binary_digits)

#converting to base 10 
base_10 = int(binary_digits, 2)
print(base_10)