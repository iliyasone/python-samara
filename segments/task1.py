print('start')
m = 0
for l in range(-100, 100):
    for r in range(l, 100):

        flag = True

        for x in range(-100, 100):
            # Q = [21, 57]
            # x in Q
            # (21 <= x and x <= 57) == (21 <= x <= 57)
            # x in P = [3, 28]
            if ((21 <= x <= 57) <= (3 <= x <= 38)) <= (not (l <= x <= r)):
                pass
            else:
                flag = False
                break

        if flag:
            if r - l < m:
                m = r - l
print(m)