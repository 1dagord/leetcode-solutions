"""
    [HARD]
    42. Trapping Rain Water

    Concepts:
    - array
    - prefix/suffix maximum

    Stats:
        Runtime | 27 ms     [Beats 30.96%]
        Memory  | 19.35 MB  [Beats 29.15%]
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0

        # prefix and suffix max
        pref = height[:]
        suff = height[:]

        for i in range(1, n):
            pref[i] = max(pref[i], pref[i-1])
            suff[n-1-i] = max(suff[n-i], suff[n-1-i])

        # ignore first and last indices
        # as no water can be held here
        for i in range(1, n-1):
            water += (min(pref[i], suff[i]) - height[i])

        return water
    