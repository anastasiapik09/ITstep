# 1. Напишіть програму для роботи онлайн магазину.
pillow = 0
blanket = 0
lamp = 0
keychain = 0

print("== ОНЛАЙН МАГАЗИН ==")
print("1. Додати товар")
print("2. Видалити товар")
print("3. Очистити кошик")
print("4. Показати кошик та суму покупки")
print("5. Вихід")

while True:
    action = input("\nВиберіть номер дії: ")

    if action == "1":
        product = input("Введіть назву товару (подушка, ковдра, лампа, брелок): ")
        quantity = int(input("Введіть кількість: "))

        if quantity <= 0:
            print("Неправильна кількість!")

        elif product == "подушка":
            pillow = pillow + quantity
            print("Товар додано!")

        elif product == "ковдра":
            blanket = blanket + quantity
            print("Товар додано!")

        elif product == "лампа":
            lamp = lamp + quantity
            print("Товар додано!")

        elif product == "брелок":
            keychain = keychain + quantity
            print("Товар додано!")

        else:
            print("Такого товару немає!")

    elif action == "2":
        product = input("Введіть назву товару для видалення: ")
        quantity = int(input("Введіть кількість: "))

        if quantity <= 0:
            print("Неправильна кількість!")

        elif product == "подушка":
            if quantity <= pillow:
                pillow = pillow - quantity
                print("Товар видалено!")
            else:
                print("Недостатньо товару в кошику!")

        elif product == "ковдра":
            if quantity <= blanket:
                blanket = blanket - quantity
                print("Товар видалено!")
            else:
                print("Недостатньо товару в кошику!")

        elif product == "лампа":
            if quantity <= lamp:
                lamp = lamp - quantity
                print("Товар видалено!")
            else:
                print("Недостатньо товару в кошику!")

        elif product == "брелок":
            if quantity <= keychain:
                keychain = keychain - quantity
                print("Товар видалено!")
            else:
                print("Недостатньо товару в кошику!")

        else:
            print("Такого товару немає!")

    elif action == "3":
        pillow = 0
        blanket = 0
        lamp = 0
        keychain = 0
        print("Кошик очищено!")

    elif action == "4":
        print("\n== ВАШ КОШИК ==")
        print("Подушка:", pillow)
        print("Ковдра:", blanket)
        print("Лампа:", lamp)
        print("Брелок:", keychain)

        total = pillow * 650 + blanket * 1700 + lamp * 500 + keychain * 60

        print("Сума покупки:", total, "грн")

    elif action == "5":
        print("Дякуємо за покупку!")
        break

    else:
        print("Неправильно вибрано дію!")
