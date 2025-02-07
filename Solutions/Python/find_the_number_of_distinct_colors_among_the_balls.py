"""
    [MEDIUM]
    3160. Find the Number of Distinct Colors Among the Balls

    Concepts:
    - array
    - hash table

    Stats:
        Runtime | 64 ms     [Beats 84.31%]
        Memory  | 63.46 MB  [Beats 28.34%]
"""

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = [0]*(len(queries))
        colors = {} # color |-> number of balls
        balls = {}  # ball |-> color

        for i, (b, c) in enumerate(queries):
            if b in balls:
                # if last ball of its color...
                if colors[balls[b]] == 1:
                    del colors[balls[b]]
                else:
                    colors[balls[b]] -= 1

            # set new color
            balls[b] = c
            colors[c] = colors.get(c, 0) + 1

            res[i] = len(colors)

        return res
