"""
    [MEDIUM]
    2349. Design a Number Container System

    Concepts:
    - design
    - hash table
    - heap/priority queue

    Stats:
        Runtime | 111 ms    [Beats 77.94%]
        Memory  | 76.44 MB  [Beats 81.37%]
"""

from collections import defaultdict
import heapq

class NumberContainers:

    def __init__(self):
        self.container = {} # index |-> number
        self.numbers = defaultdict(list) # number |-> list of indices

    def change(self, index: int, number: int) -> None:
        # insert or replace number
        self.container[index] = number
        # push to heap
        heapq.heappush(self.numbers[number], index)

    def find(self, number: int) -> int:
        h = self.numbers[number]
        while h and self.container[h[0]] != number:
            heapq.heappop(h)
        return h[0] if h else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)