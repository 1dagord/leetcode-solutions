class Trie:
    """
        Trie/Prefix Tree

        Useful for searching for words in data structures
        with lots of characters
    """
    def __init__(self):
        self.nodes = {}


    def insert(self, word: str) -> None:
        """
            Insert word into trie

            :param word: string to be inserted
        """
        curr = self.nodes

        for c in word:
            if c not in curr:
                # adds each character to nodes
                curr[c] = {}
            curr = curr[c]

        # once entire word has been added, set to True
        curr[None] = None


    def search(self, word: str) -> bool:
        """
            Search for word in trie

            :param word: string to be found
            :return: True if whole word found, False otherwise
        """
        curr = self.nodes

        for c in word:
            # if any missing letters, return false
            if c not in curr:
                return False

            curr = curr[c]

        # true only if whole word found
        return None in curr


    def startsWith(self, prefix: str) -> bool:
        """
            Checks if sequence of chars `prefix`
            exists in trie

            :param prefix: char sequence to be searched for;
                           does not need to be whole word
            :return: True if `prefix` in trie, False otherwise
        """
        curr = self.nodes

        for c in prefix:
            if c not in curr:
                return False

            curr = curr[c]

        return True
