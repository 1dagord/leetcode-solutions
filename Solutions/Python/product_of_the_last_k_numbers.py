"""
    [MEDIUM]
    1352. Product of the Last K Numbers

    Concepts:
    - design
    - data stream

    Stats:
        Runtime | 72 ms     [Beats 18.26%]
        Memory  | 145.00 MB [Beats 5.63%]
"""

class ProductOfNumbers:

    def __init__(self):
        # store current running product and
        # index of last zero
        self.stream = [(1, -1)]

    def add(self, num: int) -> None:
        prod, zero_idx = self.stream[-1]

        # if num is not zero...
        if num:
            # append num and index of last zero
            self.stream.append((prod * num, zero_idx))
        else:
            # append num and current index
            self.stream.append((prod, len(self.stream)))

    def getProduct(self, k: int) -> int:
        curr_prod, curr_zero_idx = self.stream[-1]

        if len(self.stream) - k > curr_zero_idx:
            return (curr_prod // self.stream[-k-1][0])
        return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)