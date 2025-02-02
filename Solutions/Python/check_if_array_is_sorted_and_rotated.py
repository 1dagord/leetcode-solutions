"""
    [EASY]
    1752. Check if Array Is Sorted and Rotated

    Concepts:
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.73 MB  [Beats 47.79%]
"""

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        has_break = False
        
        for i in range(n):
            if not (nums[i] <= nums[(i + 1) % n]):
                if has_break:
                    return False
                else:
                    has_break = True

        return True