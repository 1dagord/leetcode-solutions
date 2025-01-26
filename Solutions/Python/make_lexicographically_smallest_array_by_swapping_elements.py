"""
    [MEDIUM]
    2948. Make Lexicographically Smallest Array by Swapping Elements

    Concepts:
    - array
    - sorting

    Stats:
        Runtime | 223 ms    [Beats 95.54%]
        Memory  | 95.94 MB  [Beats 5.10%]
"""

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        """
            Every subset of numbers that can be swapped
            (|num1 - num2| <= limit) will be grouped, then
            sorted

            Result will be remaining array after these operations
        """
        res = []
        groups = []
        num_to_group = {}   # number |-> groups index

        for num in sorted(nums):
            # if no groups or new number
            # does not fit in last group...
            if not groups or abs(num - groups[-1][-1]) > limit:
                groups.append(deque())

            # append new number to last group
            groups[-1].append(num)
            # assign groups index
            num_to_group[num] = len(groups) - 1

        # append sorted values based on position in group
        for num in nums:
            res.append(
                groups[
                    num_to_group[num]
                ].popleft()
            )

        return res