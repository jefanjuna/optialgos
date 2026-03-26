# Consecutive Primes

## Code Execution Time Limit: 1 second

This is a challenge on code optimisation. You need to write efficient code to meet the time constraint.

---

There are some prime numbers that are quite interesting.

For example, **41** is itself a prime number, and it can be expressed as the sum of **6 consecutive primes**:

> 2 + 3 + 5 + 7 + 11 + 13 = 41

This happens to be the **longest** sum of consecutive primes that adds to a prime ≤ 100:

| Prime | Summation                | Terms |
|-------|--------------------------|-------|
| 5     | 2 + 3                    | 2     |
| 17    | 2 + 3 + 5 + 7            | 4     |
| 23    | 5 + 7 + 11               | 3     |
| 31    | 7 + 11 + 13              | 3     |
| 41    | 2 + 3 + 5 + 7 + 11 + 13  | 6     |
|       | 11 + 13 + 17             | 3     |
| 53    | 5 + 7 + 11 + 13 + 17     | 5     |
| 59    | 17 + 19 + 23             | 3     |
| 67    | 7 + 11 + 13 + 17 + 19    | 5     |
| 71    | 19 + 23 + 29             | 3     |
| 83    | 11 + 13 + 17 + 19 + 23   | 5     |
|       | 23 + 29 + 31             | 3     |
| 97    | 29 + 31 + 37             | 3     |

---

## Task

Write a Python function, `find_prime_sum(limit)` that takes in an integer `limit` representing the upper bound. It should return the prime number that has the **longest sum of consecutive primes** within that upper bound.

---

## Examples

```
find_prime_sum(41)   # returns 41
find_prime_sum(100)  # returns 41
find_prime_sum(6767) # returns 6599
```

> 3 + 5 + 7 + 11 + ... + 257 + 263 = 6599, a sum of **55 terms**