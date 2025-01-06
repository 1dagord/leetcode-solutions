"""
    [MEDIUM]
    1769. Minimum Number of Operations to Move All Balls to Each Box

    Concepts:
    - prefix sum
    - string

    Stats:
        Runtime | 8 ms      [Beats 77.01%]
        Memory  | 18.27 MB  [Beats 6.17%]
"""

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0]*n
        pref = [0]*n
        suff = [0]*n

        # left-to-right traversal
        count = 1 if boxes[0] == "1" else 0
        for i in range(1, n):
            pref[i] = pref[i-1] + count
            count += 1 if boxes[i] == "1" else 0

        # right-to-left traversal
        count = 1 if boxes[-1] == "1" else 0
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i+1] + count
            count += 1 if boxes[i] == "1" else 0

        for i in range(n):
            res[i] = pref[i] + suff[i]
        
        return res