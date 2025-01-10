"""
    [MEDIUM]
    916. Word Subsets

    Concepts:
    - hash table
    - string

    Stats:
        Runtime | 370 ms    [Beats 61.36%]
        Memory  | 27.19 MB  [Beats 5.58%]
"""

from collecitions import Counter, defaultdict

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        universals = []
        counters1 = [Counter(word) for word in words1]

        # aggregate letters from all words in words2
        all_words = defaultdict(int)
        for word in words2:
            for char, count in Counter(word).items():
                all_words[char] = max(all_words[char], count)

        def isSubset(c1: dict, c2: dict) -> bool:
            """
                Returns True if c2 is a subset of c1
            """
            for k, v in c2.items():
                if not(k in c1 and c1[k] >= v):
                    return False

            return True

        for i, c1 in enumerate(counters1):
            if isSubset(c1, all_words):
                universals.append(words1[i])

        return universals
