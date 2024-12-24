"""
    [MEDIUM]
    146. LRU Cache

    Concepts:
    - hash table
    - linked list

    Stats:
        Runtime | 88 ms     [Beatd 97.31%]
        Memory  | 78.06 MB  [Beats 29.78%]
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}     # stores inserted keys and values
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            # replace key
            val = self.cache[key]
            del self.cache[key]
            self.cache[key] = val

            return val

        return -1

    def put(self, key: int, value: int) -> None:
        # if key in cache, update value
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value

        # maintain cache
        if len(self.cache) > self.capacity:
            # delete least recently used
            lru = next(iter(self.cache))
            del self.cache[lru]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)