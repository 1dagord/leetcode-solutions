"""
    [EASY]
    1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

    Concepts:
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.20 MB  [Beats 6.98%]
"""

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(list(sentence.split())):
            if word.startswith(searchWord):
                return i + 1

        return -1