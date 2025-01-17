"""
    [MEDIUM]
    2683. Neighboring Bitwise XOR

    Concepts:
    - bit manipulation

    Stats:
        Runtime | 260 ms    [Beats 5.11%]
        Memory  | 21.87 MB  [Beats 79.56%]
"""

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        original = [0]*n

        if n == 1:
            return not derived[0]

        # construct array based on rule set
        for i in range(n - 1):
            if derived[i]:
                original[i+1] = original[i] ^ 1
            else:
                original[i+1] = original[i]

        original[-1] = 1 ^ original[0] if derived[-1] else original[0]

        # verify array
        for i in range(n - 1):
            if (
                (derived[i] and original[i] == original[i+1]) or
                (1 ^ derived[i] and original[i] != original[i+1])
            ):
                return False

        # verify last element
        return (
            (derived[-1] == (original[-1] != original[0])) or
            ((1 ^ derived[i]) == (original[-1] == original[0]))
        )