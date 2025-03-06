"""
    [MEDIUM]
    11. Container With Most Water

    Concepts:
    - array
    - two pointers

    Stats:
        Runtime | 107 ms    [Beats 38.18%]
        Memory  | 27.67 MB  [Beats 99.95%]
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0

        n = len(height)
        left = 0
        right = n - 1

        while left < right:
            # shift in pointer with lowest height
            max_water = max(
                max_water,
                min(height[left], height[right])*(right - left)
            )
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_water