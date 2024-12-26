"""
    [MEDIUM]
    494. Target Sum

    Concepts:
    - dynamic programming
    - backtracking

    Stats:
        Runtime | 199 ms    [Beats 26.07%]
        Memory  | 38.40 MB  [Beats 28.56%]
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}

        def recurse(ind, curr):
            if ind == n:
                return int(curr == target)
            
            if (ind, curr) in dp:
                return dp[(ind, curr)]

            add = recurse(ind + 1, curr + nums[ind])
            sub = recurse(ind + 1, curr - nums[ind])

            dp[(ind, curr)] = add + sub

            return add + sub

        return recurse(0, 0)
