"""
    [MEDIUM]
    873. Length of Longest Fibonacci Subsequence

    Concepts:
    - array
    - hash table

    Stats:
        Runtime | 808 ms    [Beats 73.51%]
        Memory  | 17.78 MB  [Beats 97.68%]
"""

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        max_length = 0
        nums = set(arr)

        for i in range(n):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]

                if a + b not in nums:
                    continue

                length = 2

                while a + b in nums:
                    a, b = b, a+b
                    length += 1

                max_length = max(length, max_length)

        return max_length