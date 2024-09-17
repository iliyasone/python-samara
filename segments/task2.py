for A in range(0, 10000):
    flag = True
    for x in range(0, 100):
        if (x&49 != 0) <= ((x&41 == 0) <= (x&A != 0)):
            pass
        else:
            flag = False
            break
    if flag:
        print(A)
        break