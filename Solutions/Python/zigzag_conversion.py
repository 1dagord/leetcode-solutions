"""
    [MEDIUM]
    6. Zigzag Conversion

    Concepts:
    - string

    Stats:
        Runtime | 13 ms     [Beats 45.40%]
        Memory  | 17.82 MB  [Beats 41.03%]
"""

class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        str_dirs = []
        is_moving_down = True
        k = 0

        for i, c in enumerate(s):
            str_dirs.append((c, k))
            k += 1 if is_moving_down else -1

            if k == 0:
                is_moving_down = True
            elif k == num_rows - 1:
                is_moving_down = False

        str_dirs.sort(key=lambda x: x[1])
        return "".join([c for c, _ in str_dirs])
