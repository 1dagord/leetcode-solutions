"""
    [MEDIUM]
    79. Word Search

    Concepts:
    - matrix
    - depth-first search
    - backtracking

    Stats:
        Runtime | 855 ms    [Beats 93.76%]
        Memory  | 16.78 MB  [Beats 99.98%]
"""

from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
            DFS w/ Search Pruning

            We can automatically eliminate words that do not
            meet either of the following two criteria

            1) len(word) >= m * n
            2) count for chars in word <= count for chars in board
        """
        m, n = len(board), len(board[0])

        if (m, n) == (1, 1):
            return word == board[0][0]

        def dfs(i: int, j: int, idx: int, substr: str, visited: set[tuple]) -> bool:
            output = ""

            if substr == word:
                return substr

            visited.add((i, j))

            # if neighbor on board and contains next char in word...
            for di, dj in [(-1, 0),(0, -1),(1, 0),(0, 1)]:
                if (0 <= (ni := i + di) < m and
                    0 <= (nj := j + dj) < n and
                    (ni, nj) not in visited and
                    idx < len(word) - 1 and
                    word[idx + 1] == board[ni][nj]):

                    output = max(
                        output,
                        dfs(
                            ni,
                            nj,
                            substr + board[ni][nj],
                            idx + 1,
                            visited | {(ni, nj)}
                        )
                    )

            return output

        # prune searches based on length
        if len(word) > m * n:
            return False

        # prune searches based on char frequency
        board_counter = {}
        for i in range(m):
            for j in range(n):
                char = board[i][j]
                if char not in board_counter:
                    board_counter[char] = 1
                else:
                    board_counter[char] += 1

        word_counter = Counter(word)
        for c in word_counter:
            if c not in board_counter or board_counter[c] < word_counter[c]:
                return False

        # run dfs
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, word[0], 0, set()) == word:
                        return True

        return False