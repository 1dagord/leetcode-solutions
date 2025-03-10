"""
    [MEDIUM]
    3306. Count of Substrings Containing Every Vowel and K Consonants II

    Concepts:
    - sliding window
    - string
    - hash table

    Stats:
        Runtime | 7346 ms   [Beats 5.21%]
        Memory  | 18.70 MB  [Beats 67.05%]
"""

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowel_set = set(['a', 'e', 'i', 'o', 'u'])

        def get_at_least(k: int) -> int:
            count = 0
            start, end = 0, 0

            vowels = Counter()
            consonants = 0

            # add characters until number of consonants exceeds k
            # if consonants > k, remove chars until == k
            while end < len(word):
                if word[end] in vowel_set:
                    vowels[word[end]] += 1
                else:
                    consonants += 1

                # while consonants exceed k...
                while len(vowels) == 5 and consonants >= k:
                    count += len(word) - end
                    if word[start] in vowel_set:
                        vowels[word[start]] -= 1
                    else:
                        consonants -= 1

                    # remove non-positive counts
                    vowels = +vowels

                    start += 1

                end += 1

            return count

        return get_at_least(k) - get_at_least(k+1)