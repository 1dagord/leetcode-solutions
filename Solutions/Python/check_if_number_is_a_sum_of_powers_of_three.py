"""
    [MEDIUM]
    1780. Check if Number is a Sum of Powers of Three

    Concepts:
    - backtracking
    - math

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.80 MB  [Beats 59.96%]
"""

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # 3 ** 20 > (INT_MAX = 2**31 - 1)
        powers_of_three = [3 ** exp for exp in reversed(range(20))]
        limit_reached = False

        def backtrack(num: int):
            nonlocal limit_reached

            if not num:
                return True
            
            for i, power in enumerate(powers_of_three):
                if limit_reached:
                    return False

                if power <= num:
                    powers_of_three.remove(power)
                    if backtrack(num - power):
                        return True
                    powers_of_three.insert(i, power)

            limit_reached = True

            return False

        return backtrack(n)