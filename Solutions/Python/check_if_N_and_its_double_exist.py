"""
    [EASY]
    1346. Check If N and Its Double Exist

    Concepts:
    - array
    - hash table

    Stats:
        Runtime | 3 ms      [Beats 42.42%]
        Memory  | 17.38 MB  [Beats 45.82%]
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        counter = Counter(arr)

        for num in arr:
            if num != 0:
                if 2 * num in counter:
                    return True
            else:
                if counter[num] > 1:
                    return True

        return False