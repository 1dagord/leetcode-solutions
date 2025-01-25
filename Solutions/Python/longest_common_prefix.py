"""
    [EASY]
    14. Longest Common Prefix

    Concepts:
    - string
    - trie

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.76 MB  [Beats 54.08%]
"""

class Trie:
    def __init__(self):
        self.nodes = {}

    def insert(self, s: str) -> None:
        curr = self.nodes
        for c in s:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]

        curr[None] = None

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            if not word:
                return ""
            trie.insert(word)

        curr = trie.nodes
        pref = ""

        while len(curr) == 1 and None not in curr:
            pref += list(curr.keys())[0]
            curr = curr[pref[-1]]

        return pref