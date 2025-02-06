"""
	Shell Sort

	Sorts pairs that are distant in value
	first, then closes the value gap. Useful
	in situations where memory is costly.

	---== Time Complexity ==---
		Best Case: O(n log(n))
		Average Case: Depends on gap sequence
		Worst Case: O(n^2)

	---== Space Complexity ==---
		Worst Case: O(n)
"""

def shell_sort(arr: list[int]) -> None:
	n = len(arr)
	gap = n // 2

	while gap > 0:
		for i in range(gap, n):
			temp = arr[i]
			j = i
			while j >= gap and arr[j - gap] > temp:
				arr[j] = arr[j - gap]
				j -= gap

			arr[j] = temp
		gap //= 2
