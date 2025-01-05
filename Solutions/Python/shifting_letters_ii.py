"""
    [MEDIUM]
    2381. Shifting Letters II

    Concepts:
    - string
    - prefix sum

    Stats:
        Runtime | 66 ms     [Beats 47.42%]
        Memory  | 41.47 MB  [Beats 20.36%]
"""

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        letters = [c for c in s]
        intervals = [0]*(n+1)   # for ranges including last element

        # apply direction to start and end of ranges
        for start, end, direction in shifts:
            sign = 1 if direction else -1
            intervals[start] += 1 * sign
            intervals[end+1] -= 1 * sign

        # store prefix sum to get changes
        changes = [num for num in intervals]
        for i in range(1, n):
            changes[i] += changes[i - 1]

        # remove dummy element
        changes.pop()

        # apply changes
        for i, change in enumerate(changes):
            letters[i] = chr(
                ord("a") + (
                    ((ord(letters[i]) - ord("a") + change) + 26) % 26
                )
            )

        return "".join(letters)