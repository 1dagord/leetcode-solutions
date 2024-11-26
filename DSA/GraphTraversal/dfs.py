import ultraimport

TreeNode = ultraimport("__dir__/../DataStructures/binary_tree.py", "TreeNode")


def matrix_recursive_dfs(curr: tuple[int, int], m: int, n: int) -> None:
	"""
		2D Matrix Recursive DFS

		Explores all self-avoiding paths from (0, 0) to (m, n)

		:param curr: coordinates of starting cell
		:param m: number of rows in matrix
		:param n: number of columns in matrix
	"""
	i, j = curr

	# if at edge of matrix...
	if i == m and j == n:
		return


	for di, dj in [(0, 1), (1, 0)]:
		if (0 <= (ni := i + di) < m and
			0 <= (nj := j + dj) < n):

			matrix_recursive_dfs((ni, nj), m, n)


def matrix_iterative_dfs(curr: tuple[int, int], m: int, n: int) -> None:
	"""
		2D Matrix Iterative DFS

		Explores all self-avoiding paths from (0, 0) to (m, n)

		:param curr: coordinates of starting cell
		:param m: number of rows in matrix
		:param n: number of columns in matrix
	"""
	stack = [curr]

	while stack:
		i, j = curr = stack.pop()

		if i < m - 1:
			stack.append((i + 1, j))
		if j < n - 1:
			stack.append((i, j + 1))


def binary_recursive_dfs(curr: TreeNode) -> None:
	"""
		Binary Tree Recursive DFS

		Explores all paths from root to leaf
		in increasing sorted order

		:param curr: current TreeNode object
	"""
	if not curr:
		return

	if curr.left:
		dfs(curr.left)
	if curr.right:
		dfs(curr.right)


def binary_iterative_dfs(root: TreeNode) -> None:
	"""
		Binary Tree Iterative DFS

		Explores all paths from root to leaf
		in increasing sorted order

		:param root: TreeNode object corresponding
					 to root of entire tree
	"""
	if not root:
        return
        
    stack = [root]

    while stack:
        curr = stack.pop()

        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
