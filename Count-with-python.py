#ÖVNINGSUPPGIFTER - RÄKNING MED PYTHON

# A right  angled triangle has the catheti: a = 3 and b = 4 length units. 
# Compute the hypothenuse of the triangle. (*) Första Lösning

import math

print("Uppgift 1a")
#a = 3.0
#b = 4.0
#print(f"Längden av hypotenusan är", math.sqrt(a**2 + b**2))

#Annan version, beräkna_hypotenusa definieras som en funktion och använder math.hypot (inbyggd funktion) för att räkna ut hypotenusan. 
def beräkna_hypotenusa (a: float, b: float) -> float:
    return math.hypot(a, b)

a = 3.0
b = 4.0
hypotenusa = beräkna_hypotenusa(a, b)

print(f"Längden av hypotenusan är {hypotenusa:.1f} cm.")

#__________________________________
print("Uppgift 1b")

#Uppgift 2: b)   A right angled triangle has hypothenuse c = 7.0 and a cathetus a = 5.0 length units. 
# Compute the other cathetus and round to one decimal. (*)

a = 5.0
c = 7.0
b = math.sqrt(c**2-a**2)

print(f"Längden av den andra katetern är: {b:.1f}")

#__________________________________
print("Uppgift 2")
#2. Classification accuracy (*)
#A machine learning algorithm has been trained to predict whether or not it would rain the next day. 
# Out of 365 predictions, it got 300 correct, compute the accuracy of this model.

correct_predictions = 300
total_predictions = 365
accuracy = (correct_predictions/total_predictions)
percentage = accuracy * 100

print(f"Träffsäkerheten av ML-algoritmen är: {percentage:.1f}%")

#__________________________________
print("Uppgift 3")
