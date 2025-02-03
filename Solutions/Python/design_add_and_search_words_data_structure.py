"""
    [MEDIUM]
    211. Design Add and Search Words Data Structure

    Concepts:
    - design
    - trie
    - depth-first search

    Stats:
        Runtime | 806 ms   [Beats 93.92%]
        Memory  | 52.62 MB  [Beats 84.66%]
"""

class WordDictionary:

    def __init__(self):
        self.nodes = {}

    def addWord(self, word: str) -> None:
        curr = self.nodes

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]

        curr[None] = None

    def search(self, target: str) -> bool:
        
        def dfs(curr: dict[str], idx: int) -> bool:
            if not curr:
                return False

            # if entire target searched...
            if idx == len(target):
                return None in curr

            # if leaf reached before entire target searched...
            if target[idx] in curr:
                return dfs(curr[target[idx]], idx + 1)

            if target[idx] == ".":
                for c in curr:
                    if curr != None and dfs(curr[c], idx + 1):
                        return True

            return False

        return dfs(self.nodes, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)