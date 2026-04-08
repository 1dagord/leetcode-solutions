"""
    [MEDIUM]
    3653. XOR After Range Multiplication Queries I

    Concepts:
    - array
    - simulation

    Stats:
        Runtime | 1506 ms   [Beats 92.83%]
        Memory  | 20.13 MB  [Beats 48.61%]
"""
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = (10 ** 9) + 7
        for l, r, k, v in queries:
            for idx in range(l, r + 1, k):
                nums[idx] = nums[idx] * v % MOD
        return reduce(lambda a, b: a ^ b, nums)