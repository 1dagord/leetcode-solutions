"""
    [MEDIUM]
    3152. Special Array II

    Concepts:
    - prefix sum

    Stats:
        Runtime | 56 ms     [Beats 48.46%]
        Memory  | 47.12  MB [Beats 30.23%]
"""

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)

        res = [True]*len(queries)

        # prefix array of parity differences
        
        # parity_diff[i] is number of instances of
        # parity mismatch in range [0, n]
        parity_diff = [0]*n

        for i in range(1, n):
            parity_diff[i] = parity_diff[i - 1]
            parity_diff[i] += int(nums[i] % 2 == nums[i - 1] % 2)

        for i, (start, end) in enumerate(queries):
            if ((parity_diff[end] - (parity_diff[start] if start > 0 else 0))
                and start != end):
                res[i] = False

        return res