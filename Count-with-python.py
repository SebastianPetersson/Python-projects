#ÖVNINGSUPPGIFTER - RÄKNING MED PYTHON

# A right  angled triangle has the catheti: a = 3 and b = 4 length units. 
# Compute the hypothenuse of the triangle. (*)
import math
#a = 3
#b = 4
#print("Längden av hypotenusan är:", math.sqrt(a**2 + b**2))


# A right angled triangle has hypothenuse c = 7.0 and a cathetus a = 5.0 length units. Compute the other cathetus and round to one decimal. (*)
#a = 5.0
#c =87.0
#b = math.sqrt(c**2 - a**2)
#print(f"Längden av den andra kateten är: {b:.3f}")


#a = 3
#b = 4
#print("Längden av hypotenusan är:", math.sqrt(a**2 + b**2))


#Jag ska nu räkna ut längden på den ena kateten om den andra katetens längd är 6 och hypotenusan är 11.

a = 6
c = 11
b = math.sqrt(c**2 - a**2)
print(f"Längden av den andra kateten är: {b:.2f}")

#Svar: Längden av den andra kateten är: 8.06

