#Программа "Пирожок с сюрпризом
import random
print("Спасибо, что обратили внимание на наш пирожок с сюрпризом!")
var1 = input("\nНажмите ENTER если хотите разломать его сейчас")
var2 = random.randint(1,5)
if var2 == 1:
    print("\n\"Поздравляем, Вы выиграли автомобиль!\"")
elif var2 == 2:
    print("\n\"Поздравляем, Вы выиграли квартиру!\"")
elif var2 == 3:
    print("\n\"Поздравляем, Вы выиграли путешевствие в Африку!\"")
elif var2 == 4:
    print("\n\"Поздравляем, Вы выиграли ужин на двоих в дорогом ресторане!\"")
else:
    print("\n\"Поздравляем, Вы выиграли мешок сахара!\"")
print("Удачи и до слеующего раза!")

input("\nPress ENTER to escape")
