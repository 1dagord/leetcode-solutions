"""
    [MEDIUM]
    1524. Number of Sub-arrays With Odd Sum

    Concepts:
    - math
    - prefix sum

    Stats:
        Runtime | 35 ms     [Beats 100%]
        Memory  | 21.89 MB  [Beats 66.67%]
"""

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """
            Use prefix sum to count number of previously
            odd and even subarrays before current element
            
            ODD subarray sum + ODD element = EVEN sum
            ODD subarray sum + EVEN element = ODD sum
            EVEN subarray sum + ODD element = ODD sum
            EVEN subarray sum + EVEN element = EVEN sum
        """
        curr, odd, even = 0, 0, 1

        for val in arr:
            curr ^= val & 1
            if curr:
                odd += 1
            else:
                even += 1

        return (odd * even) % (10**9 + 7)