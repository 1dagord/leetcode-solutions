"""
    [HARD]
    862. Shortest Subarray with Sum at Least K

    Concepts:
    - monotonic queue
    - double-ended queue
    - prefix sum

    Stats:
        Runtime | 227 ms    [Beats 34.51%]
        Memory  | 31.8 MB   [Beats 53.04%]
"""

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
            Monotonic Deque w/ Prefix Sum

            We are only interested in prefix sums in
            monotonic increasing order

            1) Expand subarray until prefix sum >= k

            2) Pop from left of deque while
                sum - left_val >= k
        """
        res = float("inf")

        pref_sum = 0    # prefix sum
        q = deque()     # (prefix_sum, end_index)

        for i in range(len(nums)):
            pref_sum += nums[i]

            # update length of subarray
            # if condition met
            if pref_sum >= k:
                res = min(res, i + 1)

            # find minimum valid window
            # ending at `i` sum(q) >= k
            while q and pref_sum - q[0][0] >= k:
                pref, end = q.popleft()
                res = min(res, i - end)

            # maintain monotonic deque
            while q and q[-1][0] >= pref_sum:
                q.pop()
            q.append((pref_sum, i))

        return res if res != float("inf") else -1