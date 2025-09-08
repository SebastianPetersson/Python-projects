#Uppgift 1_____________

#i = -10
#while i <= 10:
#    print(i)
#    

#Uppgift 2_____________

#sum = 0
#n = 1
#while n <= 100:
#    sum += n
#    n += 1
#    
#print(f"Det sammanlagda talet av talen mellan 1-100 är: {sum}")
#
#sum = 0
#n = 1
#while n <= 100:
#    sum += n
#    n += 2
#
#print(f"Det sammanlagda talet av alla udda siffror är: {sum}")

#Uppgift 3____________

#import random
#
#r_num = random.randint(1, 100)
#
#print("Jag tänker på ett tal, kan du gissa vilket?")
#
#guess = None
#försök = 0

#

#while guess != r_num:
#    guess = int(input("Din siffra: "))
#    försök += 1
#    if guess < r_num:
#        print("För lågt, försök igen!")
#    elif guess > r_num:
#        print("För högt, försök igen!")
#
#print(f"Korrekt gissning! Du klarade det på {försök} försök!")

#UPPGIFT 3b

#import random
#
#num = random.randint(1, 100)
#print("Nu har programmet skapat en random siffra. Programmet ska nu gissa siffran på så få försök som möjligt.")
#
#låg = 1
#hög = 100
#försök = 0
#
#while True:
#    gissning = (låg + hög)//2
#    försök +=1
#    print(f"Gissning {försök}: {gissning}")
#
#    if gissning == num:
#        print(f"Rätt tal, Talet var {num}, du klarade det på {försök} försök!")
#        break
#    elif gissning < num:
#        låg= gissning + 1
#    else:
#        hög = gissning -1
#        

#UPPGIFT 4: Multiplikation game____________ Spel som frågar efter ett svar på multiplikationen mellan två random tal.

import random

poäng = 0
fortsätt = "ja"

while fortsätt.lower()=="ja":
    x = random.randint(1, 10)
    y = random.randint(1, 10)

    print(f"Vad blir {x} * {y}?")

    svar = int(input("Ditt svar: "))
    if svar == x * y:
        print(f"Grattis, du räknade rätt!")
        poäng += 1
    else: 
        print(f"Fel, rätt svar är {x * y}.")

    fortsätt = input("Vill du fortsätta? (ja/nej): ")

print(f"Spelet är slut, du fick {poäng} poäng!")