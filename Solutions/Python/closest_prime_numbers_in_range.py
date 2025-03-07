"""
    [MEDIUM]
    2523. Closest Prime Numbers in Range

    Concepts:
    - math
    - number theory

    Stats:
        Runtime | 1661 ms   [Beats 40.63%]
        Memory  | 35.03 MB  [Beats 26.56%]
"""

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True]*(right + 1)
        sieve[0] = sieve[1] = False

        for i in range(2, int(right ** 0.5) + 1):
            if sieve[i]:
                for j in range(i ** 2, right + 1, i):
                    sieve[j] = False

        primes = [num for num in range(left, right + 1) if sieve[num]]
        
        return (
            min(
                pairwise(primes)
                , key=lambda tup: tup[1] - tup[0]
            )
            if len(primes) > 1
            else [-1, -1]
        )