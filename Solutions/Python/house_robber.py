"""
    [MEDIUM]
    198. House Robber

    Concepts:
    - dynamic programming

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.69 MB  [Beats 68.62%]
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        # initialize to impossible value
        memo = [-1]*n

        def burgle(nums: list[int], i: int) -> int:
            # if at end of street, no money can be made
            if i < 0:
                return 0

            # if already robbed this house, take money
            # from it and all eligible houses after
            if memo[i] >= 0:
                return memo[i]

            # either rob current house and house two houses down
            # or rob next house down and every eligible house before that
            res = max(burgle(nums, i-2) + nums[i], burgle(nums, i-1))

            # once end of block reached, save loot starting from `i`
            memo[i] = res

            return res
            
        return burgle(nums, n-1)