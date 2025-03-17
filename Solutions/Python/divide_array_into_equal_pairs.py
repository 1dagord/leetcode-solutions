"""
    [EASY]
    2206. Divide Array Into Equal Pairs

    Concepts:
    - hash table
    - counting

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.75 MB  [Beats 91.41%]
"""

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return sum(
            [
                v // 2
                for k, v in Counter(nums).items()
            ]
        ) == (len(nums) // 2)