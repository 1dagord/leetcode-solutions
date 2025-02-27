"""
    [MEDIUM]
    373. Find K Pairs with Smallest Sums

    Concepts:
    - array
    - heap/priority queue

    Stats:
        Runtime | 121 ms    [Beats 32.85%]
        Memory  | 34.87 MB  [Beats 56.05%]
"""

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
            Matrix of pairs

            Run BFS on matrix until k pairs visited
        """
        queue = [(0, 0, 0)]
        pairs = []
        visited = set([(0, 0)])
        m, n = len(nums1), len(nums2)

        while queue:
            len_queue = len(queue)

            for _ in range(len_queue):
                _, i, j = heapq.heappop(queue)
                pairs.append([nums1[i], nums2[j]])

                if len(pairs) == min(k, m * n):
                    return pairs

                for di, dj in [(0, 1), (1, 0)]:
                    ni, nj = i + di, j + dj

                    if ni < m and nj < n and (ni, nj) not in visited:
                        heapq.heappush(queue, (nums1[ni] + nums2[nj], ni, nj))
                        visited.add((ni, nj))

        return pairs