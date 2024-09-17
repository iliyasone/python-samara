print("введите возраст")
age = int(input())


if age < 16:
    print("доступ запрещен")
elif age < 18:
    print("доступ ограничен [16..18)")
else: # age >= 18
    print("добро пожаловать в калькулятор")


