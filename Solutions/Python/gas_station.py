"""
    [MEDIUM]
    134. Gas Station

    Concepts:
    - array
    - greedy

    Stats:
        Runtime | 28 ms     [Beats 48.66%]
        Memory  | 22.36 MB  [Beats 99.95%]
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_tank = 0
        tank = 0
        left = 0

        for i in range(n):
            total_tank += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                left = i + 1

        return -1 if total_tank < 0 else left