"""
	Python's `heapq` module provides this functionality already. This is for instructional purposes only.


	Assuming the following variables are defined:

	nums = [2,3,4]
	arr = MinHeap(nums)	// heapq.heapify(nums) does this in-place
	val = 1

	the common heap functions are as follows:

	arr.insertVal(val)	|-> heapq.heappush(nums, val)
	arr.popVal()		|-> heapq.heappop(nums)
"""


class MinHeap:
	"""
		Creates a min heap in-place

		Can be converted to a max heap by
		negating all numbers in `data`
	"""
	def __init__(self, data=None):
		self.data = [0]
		self.size = 0

		for val in data:
			self.insertVal(val)


	def __str__(self):
		return str(self.data[1:])


	def isEmpty(self):
		return (self.size == 0)


	def _minChild(self, i: int) -> int:
		"""
			Returns index of min child
		"""
		# if only one child, return index of child
		if (i * 2) + 1 > self.size:
			return i * 2

		# if node has two children and left val < curr val...
		if self.data[i*2] < self.data[(i*2)+1]:
			return i * 2

		return (i * 2) + 1


	def _siftUp(self, i: int) -> None:
		"""
			Moves value up to maintain heap property
		"""
		while i // 2 > 0:
			if self.data[i] < self.data[i//2]:
				# swap elements
				self.data[i], self.data[i//2] = self.data[i//2], self.data[i]
			else:
				return

			i //= 2


	def _siftDown(self, i: int) -> None:
		"""
			Moves value down to maintain heap property
		"""
		# if node at i has children...
		while (i * 2) <= self.size:
			# index of min child
			min_child = self._minChild(i)

			if self.data[i] > self.data[min_child]:
				# swap elements
				self.data[i], self.data[min_child] = self.data[min_child], self.data[i]

			i = min_child


	def insertVal(self, val: int) -> None:
		"""
			Inserts `val` into heap
		"""
		self.data.append(val)
		self.size += 1
		self._siftUp(self.size)


	def popVal(self) -> int:
		"""
			Pops and returns min val off of heap

			If heap is empty, raises IndexError
		"""
		if self.size == 0:
			raise IndexError("Heap is empty")

		# min value of heap
		root = self.data[1]

		# move last value to min
		self.data[1] = self.data[self.size]
		self.data.pop()

		# update size
		self.size -= 1

		# maintain heap
		self._siftDown(1)

		return root
