"""
    [MEDIUM]
    1718. Construct the Lexicographically Largest Valid Sequence

    Concepts:
    - array
    - backtracking

    Stats:
        Runtime | 6 ms      [Beats 52.21%]
        Memory  | 17.59 MB  [Beats 98.53%]
"""

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        """
            Iterate through all numbers in reverse
            Place all numbers `n` spaces apart until end reached
        """
        res = [0]*(2*n - 1)
        visited = set()

        def solve(idx: int) -> bool:
            if idx == 2*n - 1:
                return True

            for num in reversed(range(1, n+1)):
                if num in visited:
                    continue

                # skip if index next occurrence is filled
                if num > 1 and (idx+num >= 2*n - 1 or res[idx+num]):
                    continue

                # update result
                visited.add(num)
                res[idx] = num
                if num > 1:
                    res[idx+num] = num

                # recurse
                if solve(res.index(0) if 0 in res else 2*n - 1):
                    return True

                # reset and continue iteration
                visited.remove(num)
                res[idx] = 0
                if num > 1:
                    res[idx+num] = 0

            return False

        solve(0)
        return res