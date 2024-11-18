"""
    [EASY]
    2490. Circular Sentence

    Concepts:
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.48 MB  [Beats 89.38%]
"""

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        for i, word in enumerate(words[:-1]):
            next_word = words[i+1]
            if word[-1] != next_word[0]:
                return False

        return words[0][0] == words[-1][-1]