#Бросаем монетку 100 раз и считаем)
import random
input("Нажмите ENTER для начала бросков")
turn = 0
count1 = 0
count2 = 0

while turn != 100:
    turn += 1
    penny = random.randint(1,2)
    if penny == 1:
        count1 += 1
        #print ("Выпал орел!")
    else:
        count2 += 1
        #print ("Выпала решка!")
print("\nОрел выпал %s раз!" % count1)
print("Решка выпала %s раз!" % count2)
input("\nНажмите ENTER для выхода")
