print("введите число №1: ")
a = float(input())
print("введите число №2: ")
b = float(input())

print("введите операцию /*+-")
operation = input()

if operation == '+':
    print(a+b)
elif operation == '-':
    print(a-b)
elif operation == '/':
    print(a/b)
elif operation == '*':
    print(a*b)
else:
    print('недопустимая операция')
