# 1. Користувач вводить свій вік, якщо він працездатного
# віку(18-65) то виведіть фразу «Працездатний/на», інакше «Непрацездатний/на»
age = int(input("Ввеідть свій вік: "))

if age >= 18 and age <= 65:
    print("Працездатний/на")
else:
    print("Непрацездатний/на")

# 2. До завдання 2 з попереднього заняття добавте додаткову
# перевірку: щоб отримати доступ користувач повинен ще й
# ввести правильний логін secret_login = "AliBaba"
secret_login = "AliBaba"
secret_password = "OpenSesame123"

login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login == secret_login and password == secret_password:
    print("Доступ дозволено")
else:
    print("Доступ заблоковано")

# 3. Оформіть чек покупки. Користувач вводить ціну за
# одиницю товару, кількість товару та свій вік.
# Якщо користувач неповнолітній або старший за 65 років, то застосуйте знижку 15%
price = float(input("Введіть ціну за одиницю товару: "))
quantity = int(input("Введіть кількість товару: "))
age = int(input("Введіть свій вік: "))

total = price * quantity

if age <18 or age > 65:
    discount = total * 0.15
else:
    discount = 0

final_price = total - discount

print("== ЧЕК ПОКУПКИ ==")
print("Ціна за одиницю:", price)
print("Кількість товару:", quantity)
print("Сума покупки:", total)
print("Знижка:", discount)
print("До сплати:", final_price)
print("===")

#4. Оцініть якість написаного коду, спробуйте його
#простити використавши and\or
age = 23
has_license = "так"
accidents = 0

if age >= 18 and has_license == "так" and accidents == 0:
    print("Оренда дозволена")
else:
    print("Оренда заборонена")

# 5. Напишіть програму яка запитує у користувача ціну
# покупки та виводить загальну вартість(покупки + доставка). Базова ціна доставки: 120 грн
# Знижка діє лише на доставку
price = float(input("Введіть ціну покупки: "))

delivery = 120

if price < 500:
    delivery = 120
elif price <= 1000:
    delivery = 120 * 0.95
elif price <= 2000:
    delivery = 120 * 0.8
else:
    delivery = 0

total = price + delivery

print("Ціна покупки: ", price, "грн")
print("Вартість доставки: ", delivery, "грн")
print("Загальна вартість: ", total, "грн")

# 6. Користувач вводить суму кредиту та термін у роках.
# Виберіть відсоткову ставку за такими умовами:
credit = float(input("Введіть суму кредиту в доларах: "))
year = int(input("Введіть термін кредиту в роках: "))

if credit <= 10000:
    if year <= 3:
        percent = 8
    else:
        percent = 10
elif credit < 50000:
    if year <= 3:
        percent = 12
    else:
        percent = 14
else:
    percent = 20

total = credit * (1 + percent / 100) ** year
monthly_payment = total / (year * 12)

print("Відсоткова ставка:", percent, "%")
print("Загальна сума кредиту:", total, "$")
print("Щомісячний платіж:", monthly_payment, "$")