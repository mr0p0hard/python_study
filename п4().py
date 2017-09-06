print("\t\tПрограма: Автодилер")
cost = int(input("\nВведіть вартість автомобілю без націнки, грн: "))
tax = cost * 0.2
reg = cost * 0.11
ag_cost = 1000
del_prise = 700
print("\nПодаток:", tax, "грн")
print("Реєстраційний збір:", reg, "грн")
print("Агентський збір:", ag_cost, "грн")
print("Ціна доставки:", del_prise, "грн")
print("\nВсього:", cost + tax + reg + ag_cost + del_prise, "грн")
input("\nДля виходу натисніть ENTER")
