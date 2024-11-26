class ArraySegTree():
	"""
		Array Segment Tree

		Left and right children of node i
		are 2*i and 2*i+1 respectively

		Heavily limited by memory
	"""
	def __init__(self, n):
		self.seg_tree = [0]*(4*n)


	def build(self, arr: list, v: int, tl: int, tr: int) -> None:
		"""
			Builds an array of size 4n

			:param arr: array from which seg tree is built
			:param v: index of current vertex
			:param tl: left boundary of current segment
			:param tr: right boundary of current segment
		"""
		if tl == tr:
			self.seg_tree[v] = arr[tl]
		else:
			tm = (tl + tr) // 2
			self.build(arr, v*2, tl, tm)
			self.build(arr, v*2+1, tm+1, tr)
			self.seg_tree[v] = self.seg_tree[v*2] + self.seg_tree[v*2+1]


	def get_sum(self, v: int, tl: int, tr: int, l: int, r: int) -> int:
		"""
			Returns sum of node at index `v`

			:param v: node from which to compute sum
			:param tl: left boundary of current segment
			:param tr: right boundary of current segment
			:param l: left boundary of query
			:param r: right boundary of query

			:return: sum of `self.seg_tree` in range [l, r]
		"""
		if l > r:
			return 0

		if l == tl and r == tr:
			return self.seg_tree[v]

		tm = (tl + tr) // 2

		# add sum of subtrees recursively
		return (self.get_sum(v*2, tl, tm, l, min(r, tm)) +
				self.get_sum(v*2+1, tm+1, tr, max(l, tm+1), r))


	def update(self, v: int, tl: int, tr: int, pos: int, new_val: int) -> None:
		"""
			Update subtree rooted at index `v`

			:param v: current vertex
			:param tl: left boundary of current segment
			:param tr: right boundary of current segment
			:param pos: position of new element
			:param new_val: value of new element
		"""
		if tl == tr:
			self.seg_tree[v] = new_val
		else:
			tm = (tl + tr) // 2
			if pos <= tm:
				self.update(v*2, tl, tm, pos, new_val)
			else:
				self.update(v*2+1, tm+1, tr, pos, new_val)
			self.seg_tree[v] = self.seg_tree[v*2] + self.seg_tree[v*2+1]


class DynamicSegTree():
	"""
		Dynamically Allocated Object-based Segment Tree

		Nodes are only added to tree as needed
	"""
	def __init__(self):
		pass
