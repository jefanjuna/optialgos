import math
def find_prime_sum(limit):
    if limit < 2:
        return None
    size = (limit + 1) // 2
    sieve = bytearray([1]) * size
    sieve[0] = 0
    for i in range(1, math.isqrt(limit) // 2 + 1):
        if sieve[i]:
            p = 2 * i + 1
            for j in range(p * p // 2, size, p):
                sieve[j] = 0
    primes = [2] + [2 * i + 1 for i in range(1, size) if sieve[i]]
    p_sum = [0] * (len(primes) + 1)
    for i, j in enumerate(primes):
        p_sum[i + 1] = p_sum[i] + j
    def is_prime(n):
        if n == 2: return True
        if n < 2 or n % 2 == 0: return False
        return bool(sieve[n // 2])
    best_p = None
    length = 0
    for i in range(len(primes)):
        if i + length >= len(primes):
            break
        for j in range(i + length, len(primes)):
            total = p_sum[j + 1] - p_sum[i]
            if total > limit:
                break
            if is_prime(total):
                length = j - i + 1
                best_p = total
    return best_p