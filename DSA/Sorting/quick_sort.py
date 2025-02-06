"""
	Quick Sort

	Recursively splits array into
	partitions less than and greater than
	the pivot value


	---== Time Complexity ==---
		Best Case: O(n log(n))
		Average: O(n log(n))
		Worst Case: O(n^2)

	---== Space Complexity ==---
		Worst Case: O(n)
"""

def partition(arr: list[int], low: int, high: int) -> int:
	pivot = arr[high]
	i = low - 1

	for j in range(low, high):
		if arr[j] < pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]

	return i + 1

def quick_sort(arr: list[int], low: int, high: int) -> None:
	if low < high:
		pivot = partition(arr, low, high)

		quick_sort(arr, low, pivot - 1)
		quick_sort(arr, pivot + 1, high)
