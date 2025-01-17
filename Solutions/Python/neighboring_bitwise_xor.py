"""
    [MEDIUM]
    2683. Neighboring Bitwise XOR

    Concepts:
    - bit manipulation

    Stats:
        Runtime | 211 ms    [Beats 5.11%]
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
            original[i+1] = original[i] ^ derived[i]

        original[-1] = original[0] ^ derived[-1]

        # verify array
        for i in range(n - 1):
            if (derived[i] != original[i] ^ original[i+1]):
                return False

        # verify last element
        return (derived[-1] == (original[-1] ^ original[0]))