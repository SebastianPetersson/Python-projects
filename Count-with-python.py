# A right  angled triangle has the catheti: a = 3 and b = 4 length units. 
# Compute the hypothenuse of the triangle. (*)
import math
math.sqrt(3**2 + 4**2)
a = 3
b = 4
print("Längden av hypotenusan är:", math.sqrt(a**2 + b**2))


# A right angled triangle has hypothenuse c = 7.0 and a cathetus a = 5.0 length units. Compute the other cathetus and round to one decimal. (*)
a = 5.0
c = 7.0
b = math.sqrt(c**2 - a**2)
print("Längden av den andra kateten är:", round(b, 1))
