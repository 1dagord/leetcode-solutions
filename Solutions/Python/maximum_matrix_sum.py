"""
    [MEDIUM]
    1975. Maximum Matrix Sum

    Concepts:
    - matrix
    - greedy

    Stats:
        Runtime | 89 ms     [Beats 56.81%]
        Memory  | 25.09 MB  [Beats 37.60%]
"""

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_val = float("inf")
        sum_val = 0
        neg_count = 0

        for row in matrix:
            for item in row:

                if item < 0:
                    neg_count += 1

                # store smallest value
                min_val = min(min_val, abs(item))
                sum_val += abs(item)

        # if odd amount of negs, every item can be flipped
        if neg_count % 2 == 0:
            return sum_val

        # else, keep smallest item as only negative
        # subtract once to remove, twice to negate
        return sum_val - 2 * min_val