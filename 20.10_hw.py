# 1. Користувач вводить 2 числа, потрібно вивести середнє арифметичне. Але програма не працює
#Додати float, поділити потрібно на 2, замінити множення додаванням
num1 = float(input("Перше число: "))
num2 = float(input("Друге число: "))

sum = num1 + num2
average = sum / 2

print("Сума: ", sum)
print("Середнє: ", average)

# 2. Користувач вводить суму в гривнях та курс долара.
# Переведіть гривні в долари та виведіть на екран
hryvnias = float(input("Введіть суму в гривнях: "))
course = float(input("Введіть курс долара: "))

dollars = hryvnias * course
print("Сума в доларах: ", dollars)

# 3. Користувач вводить ціну товару та відсоток знижки.
# Виведіть суму знижки
price = float(input("Введіть ціну товару: "))
discount = float(input("Введіть відсоток знижки: "))

sum_discount = price * discount / 100
print("Сума знижки: ", sum_discount, "грн")

# 4. Напишіть код який обчислює окремо кількість калорій
# спалених під час цих активностей.
# Також виведіть загальну кількість спалених калорій.

slow = float(input("Час повільної ходьби (хв): "))
fast = float(input("Час швидкої ходьби (хв) :"))
run = float(input("Час легкого бігу (хв): "))

slow_calories = slow * 3
fast_calories = fast * 4.5
run_calories = run * 9

total_calories = slow_calories + fast_calories + run_calories
print("Калорії під час повільної ходьби: ", slow_calories)
print("Калорії під час швидкої ходьби", fast_calories)
print("Калорії під час легкого бігу", run_calories)
print("Загальна кількість калорій: ", total_calories)