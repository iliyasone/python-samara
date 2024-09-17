print("Задание №3")
n = int(input("Пожалуйста, введите любое целое число: "))
summa = 0
for z in range(2, n + 1):
    if z % 2 == 0:
        summa += z
        print(z)
print(summa)
