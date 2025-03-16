"""
    [MEDIUM]
    2594. Minimum Time to Repair Cars

    Concepts:
    - array
    - binary search

    Stats:
        Runtime | 1123 ms   [Beats 23.30%]
        Memory  | 25.30 MB  [Beats 6.61%]
"""

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair_in_time(time_taken: int) -> bool:
            # return True if given `time_taken`, at least
            # `cars` cars can be repaired
            get_num_cars = lambda rank: int(sqrt(time_taken / rank))
            return sum([get_num_cars(rank) for rank in ranks]) >= cars

        res = 0
        # search space upper bound is amount of time
        # it would take a single mechanic to 
        # repair all cars
        l, r = 1, max(ranks) * (cars ** 2)
        
        while l <= r:
            m = (l + r) // 2

            if can_repair_in_time(m):
                res = m
                r = m - 1
            else:
                l = m + 1

        return res