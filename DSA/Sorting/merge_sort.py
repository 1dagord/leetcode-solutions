def merge(left: list[int], right: list[int]):
	"""
		Merges two sublists

		:param left: left sublist
		:param right: right sublist

		:return: joined list
	"""
	res = []

	while left and right:
		if left[0] < right[0]:
			res.append(left[0])
			left.pop(0)
		else:
			res.append(right[0])
			right.pop(0)

	# append any remaining elements
	while left:
		res.append(left[0])
		left.pop(0)
	while right:
		res.append(right[0])
		right.pop(0)

	return res


def mergeSort(nums: list[int]):
	"""
		Recursively splits list into sublists
		until sublist size is 1, then rebuilds
		list from sorted sublists

		:param nums: list to be sorted

		:return: sorted list
	"""
	n = len(nums)

	# if list is trivially sorted...
	if n <= 1:
		return nums

	# divide into sublists
	left, right = [], []
	for i, num in enumerate(nums):
		if i < n // 2:
			left.append(num)
		else:
			right.append(num)

	# recursively sort sublists
	left = mergeSort(left)
	right = mergeSort(right)

	return merge(left, right)
