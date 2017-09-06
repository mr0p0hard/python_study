#Program "The generator of character"
#Have 30 points to increase 4 abilities
#Set variables
pool = 30
health = 0
strengh = 0
intelligense = 0
agility = 0
choise = ""
print("Hello! Bla-bla-bla, you have 30 points, choose which abilities you want to increase!")
print ("""1. Increase
2. Decrease
0. Exit""")

while choise!= 0:
    print("pool:",pool,";"
          "health:",health,";"
          "strengh:",strengh,";"
          "intelligense:",intelligense,";"
          "agility:",agility)
    choise = int(input("Make your choise: "))
    if choise == 1:
        print("""1. \"health\"
2. \"strengh\"
3. \"intelligense\"
4. \"agility\"""")
        choise2 = int(input("Choose ability:"))
        choise3 = int(input("Type sum of points: "))
        if choise2 == 1:
            pool -= choise3
            health += choise3
        elif choise2 == 2:
            pool -= choise3
            strengh += choise3
        elif choise2 == 3:
            pool -= choise3
            intelligense += choise3
        elif choise2 == 4:
            pool -= choise3
            agility += choise3
        else:
            print("Sorry, wrong number!")
    elif choise == 2:
        print("""1. \"health\"
2. \"strengh\"
3. \"intelligense\"
4. \"agility\"""")
        choise2 = int(input("Choose ability:"))
        choise3 = int(input("Type sum of points: "))
        if choise2 == 1:
            pool += choise3
            health -= choise3
        elif choise2 == 2:
            pool += choise3
            strengh -= choise3
        elif choise2 == 3:
            pool += choise3
            intelligense -= choise3
        elif choise2 == 4:
            pool += choise3
            agility -= choise3
        else:
            print("Sorry, wrong number!")
    else:
        print("Sorry, wrong number!")
    if pool < 0 or health < 0 or strengh < 0 or intelligense < 0 or agility < 0:
        print("Sorry, but pool can`t be <0! Please try again!")
        break

print("Thanls for play, hope you enjoed!")
input("Press ENTER to exit")
