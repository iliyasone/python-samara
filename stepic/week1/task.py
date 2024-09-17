A = list(map(int, input().split()))
B = list(map(int, input().split()))

fishes = []

count = 0

for i in range(len(A)):
    if B[i] == 1:  #   ->
        fishes.append(A[i])
        continue
    else:  # B[i] == 0: <-
        while fishes:
            if fishes[-1] > A[i]:
                break
            elif A[i] > fishes[-1]:
                fishes.pop()
            else:
                count += 1
        else:
            count += 1

print(count + len(fishes))
