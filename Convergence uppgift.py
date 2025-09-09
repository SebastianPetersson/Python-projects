import math

#sum = 1
#n = 1
#
#antal_steg= 10
#
#while n < antal_steg:
#    sum += 1 / (2**n)
#    n += 1
#
#print(f"Summan efter {antal_steg} steg är {sum:.2f}.")

print("Nästa uppgift: \n")

sum = 0
n = 0
antal_steg = 1000

while n < antal_steg:
    sum += ((-1)**n) / (2*n + 1)
    n += 1

print(f"Summan efter {antal_steg} steg är {sum:.5f}")