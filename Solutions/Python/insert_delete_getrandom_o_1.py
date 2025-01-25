"""
    [MEDIUM]
    380. Insert Delete GetRandom O(1)

    Concepts:
    - design
    - hash table

    Stats:
        Runtime | 168 ms    [Beats 35.67%]
        Memory  | 55.79 MB  [Beats 99.98%]
"""

class RandomizedSet:

    def __init__(self):
        self.set = set()
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set.add(val)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        try:
            self.set.remove(val)
            self.list.remove(val)
            return True
        except KeyError:
            return False

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()