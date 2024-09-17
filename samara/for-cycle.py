"""цикл for -- 
это цикл по ПОСЛЕДОВАТЕЛЬНОСТЯМ"""

eatable = ("яблоко", "банан", "вишня")
for eat in eatable:
    print(eat)
# яблоко
# банан
# вишня


for s in "прив":
    print(s)
# п
# р
# и
# в


s = 0
for i in range(5): # range(5) == (0, 1, 2, 3, 4)
    print(i)
    s += i
print(s)