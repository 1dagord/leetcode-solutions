"""
    [MEDIUM]
    57. Insert Interval

    Concepts:
    - array

    Stats:
        Runtime | 7 ms      [Beats 8.27%]
        Memory  | 19.86 MB  [Beats 20.43%]
"""

class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        intervals.append(new_interval)
        
        n = max([item for pair in intervals for item in pair])
        res = []
        singles = set() # length-1 intervals
        pref = [0]*(n + 1)
        suff = [0]*(n + 1)

        # mark start and end of each interval
        for start, end in intervals:
            if start == end:
                singles.add(start)

            pref[start] += 1
            pref[end] -= 1

            suff[end] += 1
            suff[start] -= 1

        # run prefix and suffix sum on overlaps
        for i in range(1, len(pref)):
            pref[i] += pref[i-1]
            suff[n-i] += suff[n-i+1]

        # store merged intervals
        rng = []
        for i in range(len(pref)):
            if pref[i] and not suff[i]:
                # begin range
                rng = [i]
            elif not pref[i] and suff[i]:
                # end range
                res.append(rng + [i])
                rng.clear()
            elif not pref[i] and not suff[i]:
                # length-1 range
                if i in singles:
                    res.append([i, i])
            
        return res