"""
    [HARD]
    127. Word Ladder

    Concepts:
    - string
    - hash table
    - breadth-first search

    Stats:
        Runtime | 5287 ms   [Beats 12.73%]
        Memory  | 22.18 MB  [Beats 21.22%]
"""

from collections import deque

class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        word_set = set(word_list)
        ord_a = ord("a")

        if end_word not in word_set:
            return 0

        # bfs
        queue = deque([(begin_word, 1)])
        visited = set()

        while queue:
            len_q = len(queue)

            for _ in range(len_q):
                curr, count = queue.popleft()
                visited.add(curr)

                if curr == end_word:
                    return count

                letters = [c for c in curr]

                for i, c in enumerate(letters):
                    for j in range(26):
                        letters[i] = chr(((ord_a + j) % 26) + ord_a)
                        new_word = "".join(letters)

                        if (new_word in word_set and
                            new_word not in visited):

                            queue.append((new_word, count + 1))

                    # reset letters
                    letters[i] = c

        return 0
