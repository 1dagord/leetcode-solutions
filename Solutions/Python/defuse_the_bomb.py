"""
    [EASY]
    1652. Defuse the Bomb

    Concepts:
    - array

    Stats:
        Runtime | 1 ms      [Beats 61.98%]
        Memory  | 16.7 MB   [Beats 62.03%]
"""

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0]*n
        isFlipped = False

        if not k:
            return res
            
        if k < 0:
            k *= -1
            code = code[::-1]
            isFlipped = True

        curr_sum = sum(code[1:k+1])

        for i in range(n):
            res[i] = curr_sum
            
            curr_sum -= code[(i + 1) % n]
            curr_sum += code[(k + i + 1)%n]

        return res if not isFlipped else res[::-1]