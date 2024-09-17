# EGE 100 ballov :)

from functools import cache

n = int(input())
processes = []
for i in range(n):
    t, *dependencies = map(int, input().split())
    processes.append(
        (t, dependencies)
    )
    
@cache
def when_stop(i: int):
    process = processes[i-1]
    if not process[1]:
        return process[0]
    return process[0] + max(when_stop(j) for j in process[1])


print(max(when_stop(i) for i in range(n)))    