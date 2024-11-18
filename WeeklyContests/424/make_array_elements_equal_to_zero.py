"""
    [EASY]
    3354. Make Array Elements Equal to Zero

    Concepts:
    - array

    Stats:
        Runtime | 3491 ms   [Beats 100%]
        Memory  | 16.4 MB   [Beats 100%]
"""

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        """
            Imagine brickbreaker

            return number of possible ways to clear the board
            if impossible, return -1
        """
        n = len(nums)

        def simulate(i, direc, arr):

            while 0 <= i < n:
                if arr[i] > 0:
                    arr[i] -= 1
                    direc *= -1

                i += direc

            return int(not any(arr))

        count = 0
        for i in range(n):
            if nums[i] == 0:
                count += simulate(i, 1, [num for num in nums])
                count += simulate(i, -1, [num for num in nums])

        return count