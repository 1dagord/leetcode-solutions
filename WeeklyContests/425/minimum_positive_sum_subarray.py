"""
    [EASY]
    3364. Minimum Positive Sum Subarray

    Concepts:
    - array
    - sliding window

    Stats:
        Runtime | 25 ms     [Beats 100%]
        Memory  | 16.64 MB  [Beats 100%]
"""

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        """
            `l` and `r` are min and max sliding window length
            (horribly phrased question)
        """
        min_sum = float("inf")
        n = len(nums)
        window = l
        nums += [0]

        while window <= r:
            subarr_sum = sum(nums[:window])
            for i in range(n - window + 1):

                if subarr_sum > 0:
                    min_sum = min(subarr_sum, min_sum)

                subarr_sum += nums[i+window]
                subarr_sum -= nums[i]

            window += 1

        return min_sum if min_sum != float("inf") else -1
