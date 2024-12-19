"""
    [MEDIUM]
    769. Max Chunks To Make Sorted

    Concepts:
    - array
    - greedy
    - sorting

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.75 MB  [Beats 14.45%]
"""

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
            Observe that in order for a chunk to be valid,
            it must contain numbers strictly greater than
            all numbers in the previous chunk

            In other words, min(chunk[i]) < max(chunk[i+1])

            1) Iterate over array while keeping track of
                max element up to current index
            2) If max element is at current index, then
                all previous elements are less than current
                element; increment chunks
        """
        n = len(arr)
        chunks, max_elem = 0, 0

        for i in range(n):
            max_elem = max(max_elem, arr[i])
            if max_elem == i:
                chunks += 1

        return chunks