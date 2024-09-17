intervals = input().split(',')
result = []
for interval in intervals:
    if '-' in interval:
        a, b = map(int, interval.split('-'))
        result.extend(range(a, b+1))
    else:
        result.append(interval)
print(*result)
