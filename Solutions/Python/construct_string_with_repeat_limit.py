"""
    [MEDIUM]
    2182. Construct String With Repeat Limit

    Concepts:
    - string
    - hash table
    - heap/priority queue

    Stats:
        Runtime | 215 ms    [Beats 69.88%]
        Memory  | 19.71 MB  [Beats 14.95%]
"""

import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeat_limit: int) -> str:
        counter = Counter(s)
        res = []

        # reverse letter for heap, unreverse when popping
        heap = [(-ord(letter), count)
                for letter, count in counter.items()]
        heapq.heapify(heap)

        while heap:
            letter, count = heapq.heappop(heap)
            char = chr(-letter)
            num = min(count, repeat_limit)

            res.append(char * num)
            count -= num

            if count:
                if not heap:
                    break
                next_char, next_count = heapq.heappop(heap)
                res.append(chr(-next_char))
                next_count -= 1

                if next_count:
                    heapq.heappush(heap, (next_char, next_count))
                heapq.heappush(heap, (-ord(char), count))


        return "".join(res)