a = '10'
b = 20

print('это имя a:', a)
print('это имя b:', b)


a, b = b, a
print()

print('это имя a:', a)
print('это имя b:', b)

b = int(b)
print(a + b)
