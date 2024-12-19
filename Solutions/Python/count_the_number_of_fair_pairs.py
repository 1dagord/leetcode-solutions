"""
    [MEDIUM]
    2563. Count the Number of Fair Pairs

    Concepts:
    - binary search
    - sorting

    Stats:
        Runtime | 211 ms    [Beats 65.82%]
        Memory  | 30.58 MB  [Beats 80.27%]
"""

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
            bisect_left(array, target, low, high)

            Returns index of `array` within range [low, high) 
            where every value in array[:index] < `target`
            and every value in array[index:] >= `target`


            bisect_right(array, target, low, high)

            Returns index of `array` within range [low, high) 
            where every value in array[:index] <= `target`
            and every value in array[index:] > `target`
        """
        nums.sort()
        count = 0

        for i in range(len(nums) - 1):
            low = bisect_left(nums, lower - nums[i], i + 1)
            up = bisect_right(nums, upper - nums[i], i + 1)
            count += up - low

        return count