#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

int count_divisors(int n) {
    int divs = 0;
    for (int d = 1; d <= (int)sqrt(n); d++) {
        if (n % d == 0) {
            divs += 2;
            if (d == n / d) {
                divs--;
            }
        }
    }
    return divs;
}

bool* sieve(int n) {
    bool *is_prime = (bool*)malloc((n + 1) * sizeof(bool));
    if (is_prime == NULL) {
        printf("Memory allocation failed!\n");
        exit(1);
    }

    for (int i = 0; i <= n; i++) {
        is_prime[i] = true;
    }
    is_prime[0] = is_prime[1] = false;

    for (int i = 2; i <= (int)sqrt(n); i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i) {
                is_prime[j] = false;
            }
        }
    }

    return is_prime;
}

int main() {
    int l, r;
    scanf("%d %d", &l, &r);

    int sqrt_r = (int)sqrt(r);

    int *result = (int*)malloc((sqrt_r + 1) * sizeof(int));
    int res_size = 0;

    while (sqrt_r >= 1) {
        int sq = sqrt_r * sqrt_r;
        if (sq < l || sq <= 1) {
            break;
        }

        int divs = count_divisors(sqrt_r);
        result[res_size++] = divs * 2 - 1;
        sqrt_r--;
    }

    if (res_size == 0) {
        printf("0\n");
        free(result);
        return 0;
    }

    int max_val = 0;
    for (int i = 0; i < res_size; i++) {
        if (result[i] > max_val) {
            max_val = result[i];
        }
    }

    bool *primes = sieve(max_val);

    int ans = 0;
    for (int i = 0; i < res_size; i++) {
        if (primes[result[i]]) {
            ans++;
        }
    }

    printf("%d\n", ans);

    free(result);
    free(primes);

    return 0;
}
