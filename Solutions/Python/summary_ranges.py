"""
    [EASY]
    228. Summary Ranges

    Concepts:
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.58 MB  [Beats 90.86%]
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums or len(nums) == 1:
            return [str(num) for num in nums]

        ranges = []
        rng = str(nums[0])

        for i in range(1, len(nums)):
            last_num = str(nums[i-1])
            curr_num = str(nums[i])

            # if discontinuous ranges
            if nums[i] - nums[i-1] != 1:
                if rng != last_num:
                    rng += "->" + last_num
                ranges.append(rng)
                rng = curr_num

            # if at end of list
            if i == len(nums) - 1:
                if rng != curr_num:
                    rng += "->" + curr_num
                ranges.append(rng)

        return ranges