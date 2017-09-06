import random
WORDS =("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = random.choice(WORDS)
print ( "\Количество букв в загаданном слове составляет:", len(word))
trying = 1
while trying <= 5:
    var = input( "Введите предполагаемую букву: ")
    trying +=1
    if var in word:
        print("Да")
    else :
        print("Нет")
correct = input("Попробуйте угадать слово: ")
if correct == word:
    print ("Да! Вы победили! Позравляем!")
else:
    print ("Нет. Мне жаль. Вы проиграли.")
input("\n\nHaжмитe Enter. чтобы выйти.")
