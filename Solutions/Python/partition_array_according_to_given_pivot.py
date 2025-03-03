"""
    [MEDIUM]
    2161. Partition Array According to Given Pivot

    Concepts:
    - array
    - simulation

    Stats:
        Runtime | 20 ms     [Beats 96.11%]
        Memory  | 34.47 MB  [Beats 83.89%]
"""

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lt, eq, gt = [], [], []

        for num in nums:
            if num < pivot:
                lt.append(num)
            elif num > pivot:
                gt.append(num)
            else:
                eq.append(num)

        return lt + eq + gt