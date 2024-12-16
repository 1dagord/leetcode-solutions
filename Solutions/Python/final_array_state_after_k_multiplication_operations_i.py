"""
    [EASY]
    3264. Final Array State After K Multiplication Operations I

    Concepts:
    - heap/priority queue

    Stats:
        Runtime | 4 ms      [Beats 26.45%]
        Memory  | 17.32 MB  [Beats 19.20%]
"""

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        vals = [(nums, i) for i, nums in enumerate(nums)]
        heapq.heapify(vals)
        while k:
            val, i = heapq.heappop(vals)
            nums[i] = val * multiplier
            heapq.heappush(vals, (val * multiplier, i))
            k -= 1

        return nums