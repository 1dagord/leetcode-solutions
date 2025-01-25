"""
    [MEDIUM]
    274. H-Index

    Concepts:
    - sorting
    - counting sort

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.79 MB  [Beats 100%]
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0

        # maximum h-index
        n = len(citations)

        for i, num_cit in enumerate(citations):
            num_papers_w_cit = i+1
            h_index = max(h_index, min(num_papers_w_cit, num_cit))

        return h_index