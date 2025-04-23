"""
    [EASY]
    1399. Count Largest Group

    Concepts:
    - hash table
    - math

    Stats:
        Runtime | 30 ms     [Beats 66.50%]
        Memory  | 17.94 MB  [Beats 40.50%]
"""

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_digits(num: int) -> int:
            digits = []
            while num:
                digits.append(num % 10)
                num //= 10

            return sum(digits)

        digit_sums = defaultdict(set)

        for num in range(1, n + 1):
            digit_sums[sum_digits(num)].add(num)

        max_len = max(map(len, digit_sums.values()))
        return list(map(len, digit_sums.values())).count(max_len)