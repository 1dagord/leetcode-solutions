from collections import deque
import ultraimport

TreeNode = ultraimport("__dir__/../DataStructures/binary_tree.py", "TreeNode")


def matrix_iterative_bfs(curr: tuple[int, int], m: int, n: int) -> None:
	"""
		2D Matrix Iterative BFS
		
		Traverses every direct path from (0, 0) to (m-1, n-1)

		:param curr: coordinates of starting cell
		:param m: number of rows in matrix
		:param n: number of columns in matrix
	"""
	queue = deque([curr])
	visited = set([curr])

	while queue:
		len_q = len(queue)

		# iterate over children
		for _ in range(len_q):
			curr = queue.popleft()
			i, j = curr

			# check for valid moves
			for di, dj in [(0, 1), (1, 0)]:
				if (0 <= (ni := i + di) < m and
					0 <= (nj := j + dj) < n and
					(ni, nj) not in visited):

					queue.append((ni, nj))
					visited.add((ni, nj))


def binary_iterative_bfs(node: TreeNode) -> None:
	"""
		Iterative BFS on binary tree

		Traverses every path from root to leaf

		:param node: node in binary tree
	"""
	queue = deque([node])

	while queue:
		n = len(queue)

		# iterate over children
		for _ in range(n):
			curr = queue.popleft()

			# check for valid moves
			if curr.left:
				queue.append(curr.left)
			if curr.right:
				queue.append(curr.right)
