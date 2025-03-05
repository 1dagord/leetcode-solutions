"""
    [HARD]
    502. IPO

    Concepts:
    - array
    - greedy
    - heap/priority queue

    Stats:
        Runtime | 377 ms    [Beats 44.77%]
        Memory  | 42.10 MB  [Beats 82.38%]
"""

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        money = w
        max_prof = []
        min_cap = list(zip(capital, profits))
        heapq.heapify(min_cap)

        for _ in range(k):
            # push all affordable projects to max heap `max_prof`
            while min_cap and min_cap[0][0] <= money:
                c, p = heapq.heappop(min_cap)
                heapq.heappush(max_prof, -p)

            # if no affordable projects...
            if not max_prof:
                break

            # complete most profitable project
            money -= heapq.heappop(max_prof)

        return money