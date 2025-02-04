"""
    [MEDIUM]
    208. Implement Trie (Prefix Tree)

    Concepts:
    - design
    - hash table
    - string

    Stats:
        Runtime | 26 ms     [Beats 94.89%]
        Memory  | 29.93 MB  [Beats 93.89%]
"""

class Trie:

    def __init__(self):
        self.nodes = {}

    def insert(self, word: str) -> None:
        curr = self.nodes

        for c in word:
            if c not in curr:
                # adds each character to nodes
                curr[c] = {}
            curr = curr[c]

        # once entire word has been added, set to True
        curr[None] = None

    def search(self, word: str) -> bool:
        curr = self.nodes

        for c in word:
            # if any missing letters, return false
            if c not in curr:
                return False

            curr = curr[c]

        # true only if whole word found
        return None in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.nodes

        for c in prefix:
            if c not in curr:
                return False

            curr = curr[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)