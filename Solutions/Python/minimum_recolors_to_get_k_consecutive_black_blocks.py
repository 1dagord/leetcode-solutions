"""
    [EASY]
    2379. Minimum Recolors to Get K Consecutive Black Blocks

    Concepts:
    - string
    - sliding window

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.76 MB  [Beats 62.29%]
"""

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
            While iterating, count ahead k chars and store
            number of changes needed ("W"s) to make k
            consecutive "B"s
        """
        min_ops = float("inf")

        for i in range(len(blocks) - k + 1):
            window = blocks[i:i+k]
            min_ops = min(min_ops, window.count("W"))

        return min_ops