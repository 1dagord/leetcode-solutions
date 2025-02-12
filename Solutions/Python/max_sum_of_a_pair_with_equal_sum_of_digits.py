"""
    [MEDIUM]
    2342. Max Sum of a Pair With Equal Sum of Digits

    Concepts:
    - hash table
    - heap/priority queue

    Stats:
        Runtime | 265 ms    [Beats 90.52%]
        Memory  | 33.44 MB  [Beats 78.99%]
"""

from collections import defaultdict
import heapq

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = -1

        def sum_digits(num):
            res = 0
            while num:
                res += num % 10
                num //= 10
            return res

        # group numbers by sum of digits
        digits = defaultdict(list)
        for num in nums:
            heapq.heappush(digits[sum_digits(num)], -num)

        # compare largest two from each group
        for k, v in digits.items():
            if len(v) >= 2:
                max_val = max(
                    max_val,
                    -heapq.heappop(v) - heapq.heappop(v)
                )

        return max_val