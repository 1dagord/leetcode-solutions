"""
    [HARD]
    30. Substring with Concatenation of All Words

    Concepts:
    - string
    - hash table
    - depth-first search

    Stats:
        Runtime | 563 ms    [Beats 42.07%]
        Memory  | 19.14 MB  [Beats 5.69%]
"""

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(set(words)) == 1:
            words = ["".join(words)]

        word_length = len(words[0])
        all_words_length = word_length * len(words)
        s_length = len(s)

        indices = []
        remaining = Counter(words)

        def dfs(idx: int):
            nonlocal indices, remaining

            if not remaining:
                indices.append(idx - all_words_length)
                return

            word = s[idx:idx+word_length] 
            if word in remaining:
                remaining[word] -= 1
                if not remaining[word]:
                    del remaining[word]

                dfs(idx + word_length)

                remaining[word] += 1

            
        for i in range(s_length):
            if s[i:i+word_length] in remaining:
                dfs(i)

        return indices