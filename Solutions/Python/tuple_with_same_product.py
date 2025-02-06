"""
    [MEDIUM]
    1726. Tuple with Same Product

    Concepts:
    - hash table
    - counting

    Stats:
        Runtime | 1019 ms   [Beats 9.01%]
        Memory  | 134.05 MB [Beats 5.21%]
"""

from collections import defaultdict
from math import comb

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        """
            For any set of 4 comprised of 2 pairs,
            there are 8 ways to arrange the numbers

            For any set bigger than 4, arrange the numbers
            in pairs, then then arrange the sets of 4 as above

            Number of arrangements:
                8 * (m choose n)

                m := len(subset) // 2
                n := 4 // 2
        """
        count = 0
        n = len(nums)
        products = defaultdict(set)

        for i in range(n):
            for j in range(i + 1):
                products[nums[i] * nums[j]].update({i, j})

        for subset in products.values():
            if len(subset) >= 4:
                count += 8 * (comb(len(subset) // 2, 2))
        
        return count