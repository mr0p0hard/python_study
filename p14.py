#Program "Who is your daddy?"
#Show family web
#Create vokabrulary
family = {"Serhiy": ("Vladimir", "gr.Peter"),
          "Oleg": ("Oleg", "gr.Alexey"), "Bohdan": ("Evgeniy", "gr.Alexandr")}

print("OLa! Me amo pasi la de muerta!")

choise = ""
#main menu
print("""Choose action:
1.Search
2.Add
3.Change
4.Remove""")
while True:
    choise = int(input("Type: "))
    if choise == 1:
        son = input("Type name of the son: ")
        if son in family:
            print("His father`s name is: ", family[son])
        else:
            print("Data is not found")
    elif choise == 2:
        son = input("Type the name you want to add: ")
        if son not in family:
            father = input("Type the name of his father: ")
            family[son] = father
            print("Upload sucsessful!")
        else:
            print("Sorry, but this name is using in database! Try again!")
    elif choise == 3:
        son = input("Type name of the son: ")
        if son in family:
            father = input("Type the name of his realy father: ")
            family[son] = father
            print("Sucsess!")
        else:
            print("Sorry, but this name is using in database! Try again!")
    elif choise == 4:
        son = input("Type name of the removable son: ")
        if son in family:
            del family[son]
            print("Sucsess!")
        else:
            print("Sorry, but this name is using in database! Try again!")
    elif choise == 0:
        break
    else:
        print("Incorrect type! Please try again!")
print("Thanks for using! Goodbye!")
input("Type ENTER to exit!")
