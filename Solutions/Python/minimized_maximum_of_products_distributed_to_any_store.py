"""
    [MEDIUM]
    2064. Minimized Maximum of Products Distributed to Any Store

    Concepts:
    - array
    - binary search

    Stats:
        Runtime | 676 ms    [Beats 36.83%]
        Memory  | 28.70 MB  [Beats 47.59%]
"""

class Solution:
    def minimizedMaximum(self, n: int, arr: List[int]) -> int:
        if n == len(arr):
            return max(arr)

        arr.sort(reverse=True)

        def can_fit(m):
            # check if evenly distributed
            # products can fit in `n` stores
            ans = 0 
            for num in arr:
                ans += ceil(num / m)
                
            return ans <= n

        # typical binary search
        l, r = 1, arr[0]

        # use < bc searching for min element
        while l < r:
            # overflow protection
            m = l + (r - l) // 2

            if can_fit(m):
                r = m
            else:
                # if cannot fit, exclude min element
                l = m + 1
        
        return r
        