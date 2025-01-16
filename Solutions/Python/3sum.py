"""
    [MEDIUM]
    15. 3Sum

    Concepts:
    - two pointers
    - sorting

    Stats:
        Runtime | 522 ms    [Beats 77.51%]
        Memory  | 19.14 MB  [Beats 99.28%]
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
            Use two pointers, one at each end of sorted array
        """
        triplets = set()
        nums.sort()
        
        n = len(nums)

        for i in range(n):
            # skip duplicate values
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # set target to be found using other two indices
            target = -nums[i]

            j = i + 1
            k = n - 1

            while j < k:
                val = nums[j] + nums[k]

                if val == target:
                    triplets.add(tuple([nums[v] for v in [i, j, k]]))
                    j += 1
                    k -= 1
                elif val > target:
                    k -= 1
                else:
                    j += 1

        return list(triplets)

