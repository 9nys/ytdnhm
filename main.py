try:
    num1 = int(input("Введіть перше число: "))
    num2 = int(input("Введіть друге число: "))
    result = num1 / num2
    print("Результат: ", result)
except ZeroDivisionError:
    print("Помилка: Ділення на нуль!")
except ValueError:
    print("Помилка: Некоректний ввід числа!")