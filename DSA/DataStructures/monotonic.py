from collections import deque


class Monotonic:
	"""
		Stack/Queue where successive elements are strictly
		greater or less than all predecessors
	"""
	def __init__(self, name):
		self.name = name

		if self.name == "queue":
			self.iterable = deque([])
		elif self.name == "stack":
			self.iterable = []


	def build_increasing(self, values: list[int]) -> list[int]:
		"""
			Strictly increasing monotonic stack/queue

			:param values: values to be added to stack/queue

			:return: monotonically increasing stack/queue
		"""
		for val in values:
			while self.iterable and val <= self.iterable[-1]:
				self.iterable.pop()
			self.iterable.append(val)

		return self.iterable


	def build_decreasing(self, values: list[int]) -> list[int]:
		"""
			Strictly decreasing monotonic stack/queue

			:param values: values to be added to stack/queue

			:return: monotonically increasing stack/queue
		"""
		for val in values:
			while self.iterable and val >= self.iterable[-1]:
				self.iterable.pop()
			self.iterable.append(val)

		return self.iterable


	def pop_val(self) -> int:
		"""
			If queue, pops from left
			If stack, pops from right

			:return: popped value depending on
					 underlying data structure
		"""
		if self.name == "queue":
			return self.iterable.popleft()
		elif self.name == "stack":
			return self.iterable.pop()
