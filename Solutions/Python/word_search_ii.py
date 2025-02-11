"""
    [HARD]
    212. Word Search II

    Concepts:
    - matrix
    - trie
    - depth-first search

    Stats:
        Runtime | 7584 ms   [Beats 14.42%]
        Memory  | 18.65 MB  [Beats 87.71%]
"""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
            Build trie, the search trie and
            matrix using DFS
        """
        m, n = len(board), len(board[0])
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        words_on_board = []
        trie = {}

        # populate trie
        for word in words:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]

            # mark end of word
            curr[False] = False

        def dfs(
            i: int,
            j: int,
            path: list[str],
            curr: dict[dict],
            visited: set[tuple]) -> bool:
            """
                Performs DFS on board while using
                trie for guidance
            """
            nonlocal words_on_board

            if False in curr:
                words_on_board.append("".join(path))
                # set to True if word found
                del curr[False]
                curr[True] = True

            for di, dj in moves:
                ni, nj = i + di, j + dj
                if (0 <= ni < m and
                    0 <= nj < n and
                    (ni, nj) not in visited and
                    board[ni][nj] in curr):

                    dfs(
                        ni,
                        nj,
                        path + [board[ni][nj]],
                        curr[board[ni][nj]],
                        visited | {(ni, nj)}
                    )

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(
                        i,
                        j,
                        [board[i][j]],
                        trie[board[i][j]],
                        set([(i, j)])
                    )

        return words_on_board