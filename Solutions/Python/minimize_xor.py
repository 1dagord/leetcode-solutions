"""
    [MEDIUM]
    2429. Minimize XOR

    Concepts:
    - bit manipulation

    Stats:
        Runtime | 1 ms      [Beats 28.80%]
        Memory  | 17.79 MB  [Beats 41.60%]
"""

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        """
            For XOR to be minimal, must have as many of
            same bits as possible
        """
        res = num1

        # get number of set bits
        n2_set_bit_count = 0
        res_set_bit_count = 0
        for i in range(32):
            n2_set_bit_count += 1 if num2 & (1 << i) else 0
            res_set_bit_count += 1 if res & (1 << i) else 0

        # set lower bits until same number of bits set
        for bit in range(32):
            # if less bits than desired...
            if res_set_bit_count < n2_set_bit_count:
                # if bit is not set, set and update count
                if not (res & (1 << bit)):
                    res |= (1 << bit)
                    res_set_bit_count += 1
            # if more bits than desired...
            elif res_set_bit_count > n2_set_bit_count:
                # if bit is set, reset and update count
                if (res & (1 << bit)):
                    res -= (1 << bit)
                    res_set_bit_count -= 1
            else:
                break
        
        return res