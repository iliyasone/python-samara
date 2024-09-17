n = int(input())
line = list(map(int, input().split()))

for i in range(n):
    if line[i] == -1:
        if i > 0:
            line[i] = line[i - 1] + 1
        else:
            line[i] = 1

if sorted(line) == line:
    print("YES")

    result = [line[0]]
    for i in range(1, n):
        result.append(line[i] - line[i - 1])
    print(*result)
else:
    print("NO")
