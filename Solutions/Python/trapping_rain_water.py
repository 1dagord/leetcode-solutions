"""
    [HARD]
    42. Trapping Rain Water

    Concepts:
    - array
    - prefix/suffix maximum

    Stats:
        Runtime | 31 ms     [Beats 24.49%]
        Memory  | 18.39 MB  [Beats 74.02%]
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        """
            Store prefix and suffix max 
            (max of all indices before `i` and
            max of all indices after `i`)

            Take minimum of pref and suff to be tallest amount
            of water possible at indes `i`

            Diff of height[i] and min(pref[i], suff[i])
            is amount of water to be stored at index `i`
        """
        n = len(height)
        water = 0

        # prefix max and suffix max
        pref = [0]*n
        suff = [0]*n

        for i in range(1, n):
            pref[i] = max(pref[i-1], height[i-1])

        for i in range(n - 2, -1, -1):
            suff[i] = max(suff[i+1], height[i+1])

        # for each index `i`, subtract that position's
        # height from the min(pref[i], suff[i])

        for i, h in enumerate(height):
            if (drops := min(pref[i], suff[i]) - h) > 0:
                water += drops

        return water
    