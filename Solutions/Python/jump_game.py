"""
    [MEDIUM]
    55. Jump Game

    Concepts:
    - array
    - greedy

    Stats:
        Runtime | 7 ms      [Beats 97.41%]
        Memory  | 18.81 MB  [Beats 15.29%]
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goalpost = n-1
        i = n-1

        while i >= 0:
            if goalpost - i <= nums[i]:
                goalpost = i

            i -= 1

        return goalpost == 0
