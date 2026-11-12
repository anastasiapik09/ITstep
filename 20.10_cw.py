# 1. Користувач вводить радіус кола. Потрібно обрахувати  площу круга та вивести результат з двома знаками після
# коми.
#Вводимо радіус кола від користувача
radius = float(input("Введіть радіус: "))
#Задаємо значення числа пі
pi = 3.1415
#Обчислюємо площу круга за формулою pi * radius у квадраті
area = pi * radius ** 2
#Виводимо площу круга з двома знаками після коми
print(f"Площа круга: {area:.2f}")

# 2,4. Користувач вводить ціну однієї кружки та загальний
# бюджет. Виведіть скільки кружок можна купити. У завданні (2) виведіть ще залишок коштів
price = float(input("Введіть ціну однієї кружки: "))
budget = float(input("Введіть бюджет: "))

count = int(budget // price)
remainder = budget % price

print("Можна купити: ", count, "кружки")
print("Залишок коштів:", remainder, "грн")

# 3. Користувач вводить довжину в метрах. Виведіть цю довжину в футах та ярдах.
meters = float(input("Введіть довжину в метрах: "))

feet = meters * 3.2808399
yards = meters * 1.0936133

print(f"Довжина у футах: {feet:.2f}")
print(f"Довжина у ярдах: {yards:.2f}")

# 5. Користувач вводить загальну кількість хвилин.
# Переведіть їх у години та хвилини.
minutes = int(input("Введіть кількість хвилин: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print("Годин: ", hours)
print("Хвилин: ", remaining_minutes)

# 6. Щоб спекти пиріг потрібно 4 яблука та 1.2 літра молока.
# Користувач вводить кількість яблук та молока(у літрах). Виведіть скільки він може спекти пирогів.
apples = int(input("Введіть кількість яблук: "))
milk = float(input("Введіть кількість молока (л): "))


pies_apples = apples // 4
pies_milk = milk // 1.2

pies = int(min(pies_apples, pies_milk))

remaining_apples = apples - pies * 4
remaining_milk = milk - pies * 1.2

print("Можна спекти пирогів: ", pies)
print("Залишиться яблук: ", remaining_apples)
print("Залишиться молока: ", remaining_milk)

# 7. Користувач вводить суму вкладу в банк та відсоток
# ставки.
deposit = float(input("Введіть суму вкладу: "))
rate = float(input("Введіть відсоткову ставку: "))

year1 = deposit + deposit * rate / 100
print("Сума вкладу через 1 рік:", year1)

year2 = year1 + year1 * rate / 100
print("Сума вкладу через 2 роки:", year2)

year3 = year2 + year2 * rate / 100
print("Сума вкладу через 3 роки:", year3)

year4 = year3 + year3 * rate / 100
print("Сума вкладу через 4 роки:", year4)

year5 = year4 + year4 * rate / 100
print("Сума вкладу через 5 років:", year5)

# 8. Користувач вводить кількість днів. Виведіть скільки це
# років, тижнів та днів.
days = int(input("Введіть кількість днів: "))

years = days // 365
remaining_days = days % 365

weeks = remaining_days // 7
remaining_days = remaining_days % 7

print(days, "днів - це", years, "рік,", weeks, "тижні та", remaining_days, "днів.")