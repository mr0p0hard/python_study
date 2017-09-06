print("Программа \"Считалочка\"")
var1 = int(input("Введите первую цифру отсчета: "))
var2 = int(input("Введите последнюю цифру отсчета: "))
var3 = int(input("Введите шаг отсчета: "))

for i in range(var1, var2, var3):
      print (i, end = " ")

input("Для выхода нажмите ENTER")
