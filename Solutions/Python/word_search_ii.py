"""
    [HARD]
    212. Word Search II

    Concepts:
    - matrix
    - trie
    - depth-first search

    Stats:
        Runtime | 6488 ms   [Beats 32.23%]
        Memory  | 18.95 MB  [Beats 78.40%]
"""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
            Build trie, then search trie and
            matrix using DFS
        """
        m, n = len(board), len(board[0])
        words = set(words)
        words_on_board = set()
        visited = set()
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        trie = {}
        for word in words:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            # end-of-word marker
            curr[None] = None
            
        def dfs(i: int, j: int, graph: dict, word: str) -> None:
            nonlocal words_on_board, visited
            
            # if whole word found...
            if None in graph:
                words_on_board.add(word)
            
            for di, dj in moves:
                ni, nj = i + di, j + dj
                if (
                    0 <= ni < m and
                    0 <= nj < n and
                    (ni, nj) not in visited and 
                    board[ni][nj] in graph
                ):
                    visited.add((i, j))
                    dfs(ni, nj, graph[board[ni][nj]], word + board[ni][nj])
                    visited.remove((i, j))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    visited.clear()
                    dfs(i, j, trie[board[i][j]], board[i][j])
                    
        return list(words_on_board)