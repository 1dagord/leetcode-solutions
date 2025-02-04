"""
    [MEDIUM]
    322. Coin Change

    Concepts:
    - dynamic programming
    - breadth-first search

    Stats:
        Runtime | 219 ms    [Beats 99.64%]
        Memory  | 16.56 MB  [Beats 100%]
"""

from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
            BFS
        """
        # amount -> is_visited
        visited = [False] * (amount + 1)
        queue = deque([amount])

        level = 0  # Tracks the number of coins used (BFS level)

        while queue:
            # Number of elements at the current level
            len_q = len(queue)
            
            # Explore nodes at the current level
            for _ in range(len_q):
                curr_amount = queue.popleft()
                
                if curr_amount == 0:
                    return level
                
                # Check next amounts by using available coins
                for coin in coins:
                    new_amount = curr_amount - coin
                    if new_amount >= 0 and not visited[new_amount]:
                        queue.append(new_amount)
                        visited[new_amount] = True
            
            level += 1

        return -1  # If BFS is exhausted without reaching amount 0