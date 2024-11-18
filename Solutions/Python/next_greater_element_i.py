"""
    [EASY]
    496. Next Greater Element I

    Concepts:
    - monotonic stack
    - hash map

    Stats:
        Runtime | 3 ms      [Beats 46.69%]
        Memory  | 16.88 MB  [Beats 53.36%]
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        stack = []

        # if curr elem > last elem on stack, pop
        # last elem and store curr elem as next
        # highest of last elem
        for n2 in nums2:
            while stack and stack[-1] < n2:
                mp[stack.pop()] = n2
            stack.append(n2)

        # if num in map, it must have been popped off
        # stack due to next highest

        # else, assign nums1[i] to -1
        for i in range(len(nums1)):
            nums1[i] = mp.get(nums1[i], -1)

        return nums1