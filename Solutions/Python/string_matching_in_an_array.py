"""
    [MEDIUM]
    1408. String Matching in an Array

    Concepts:
    - string
    - array

    Stats:
        Runtime | 1 ms      [Beats 77.61%]
        Memory  | 17.86 MB  [Beats 34.66%]
"""

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()

        for i, word in enumerate(words):
            for j, match in enumerate(words):
                if i != j and match in word:
                    ans.add(match)

        return list(ans)