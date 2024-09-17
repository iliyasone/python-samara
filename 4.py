def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    primes = {i for i, val in enumerate(is_prime) if val}
    return primes

def count_divisors(n):
    divs = 0
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            divs += 2  
            if d == n // d:
                divs -= 1

    return divs


l, r = map(int, input().split())

sqrt = int(r**0.5)


result = []
while True:
    sq = sqrt**2
    if sq < l or sq <= 1:
        break


    divs = count_divisors(sqrt)
            
    
    # print(sq, divs*2-1)
    result.append(divs*2-1)

    sqrt -= 1

if not result:
    print(0)
else:
    primes = sieve(max(result))
    ans = 0
    for divs in result:
        if divs in primes:
            ans += 1
            
    print(ans)