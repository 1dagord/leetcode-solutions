"""
    [MEDIUM]
    1980. Find Unique Binary String

    Concepts:
    - backtracking
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.90 MB  [Beats 52.45%]
"""

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set([int(num, 2) for num in nums])

        def solve(idx: int, ans: int) -> int:
            if idx == n:
                return ans if ans not in nums else 0

            if (
                (res := solve(idx + 1, 1 | (ans << 1))) or
                (res := solve(idx + 1, (ans << 1)))
            ):
                return res

            return 0

        return bin(solve(0, 0))[2:].rjust(n, "0")