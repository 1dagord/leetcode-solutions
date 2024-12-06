"""
    [MEDIUM]
    2554. Maximum Number of Integers to Choose From a Range I

    Concepts:
    - array
    - hash table

    Stats:
        Runtime | 51 ms     [Beats 52.63%]
        Memory  | 18.98 MB  [Beats 9.90%]
"""

class Solution:
    def maxCount(self, banned: List[int], n: int, max_sum: int) -> int:
        """
            Return max number of integers that fit following criteria:
            - not in array `banned`
            - within range [1, n]
            - sum of all integers <= max_sum
        """
        banned = set(banned)
        nums = [num for num in range(1, n+1) if num not in banned]

        curr_sum = sum(nums)
        amt_nums = len(nums)

        while curr_sum > max_sum:
            amt_nums -= 1
            curr_sum -= nums[amt_nums]

        return amt_nums