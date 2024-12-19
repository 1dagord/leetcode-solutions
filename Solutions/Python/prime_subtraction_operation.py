"""
    [MEDIUM]
    2601. Prime Subtraction Operation

    Concepts:
    - math
    - binary search

    Stats:
        Runtime | 164 ms    [Beats 16.34%]
        Memory  | 16.90 MB  [Beats 55.16%]
"""

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Sieve of Eratosthenes
        primes = [i for i in range(1001)]
        for i in range(2, len(primes)):
            val = i
            idx = i + val
            while idx < len(primes):
                primes[idx] = None
                idx += val

        primes[0] = None
        primes[1] = None

        prev = 0
        for num in nums:
            upper_bound = num - prev

            largest_prime = 0
            for i in reversed(range(2, upper_bound)):
                if primes[i]:
                    largest_prime = i
                    break

            if num - largest_prime <= prev:
                return False
            prev = num - largest_prime

        return True