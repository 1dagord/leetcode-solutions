"""
    [MEDIUM]
    2981. Find Longest Special Substring That Occurs Thrice I

    Concepts:
    - string
    - sliding window

    Stats:
        Runtime | 247 ms    [Beats 5.13%]
        Memory  | 17.52 MB  [Beats 5.52%]
"""

class Solution:
    def maximumLength(self, s: str) -> int:

        spec_substr = ""
        visited = set()

        def isSpecial(substr: str, length: int) -> bool:
            char = substr[0]
            for i in range(1, length):
                if substr[i] != char:
                    return False
            return True

        window = 1
        n = len(s)

        while window < n:
            # sliding window
            for i in range(n - window + 1):
                substr = s[i:i+window]
                if substr not in visited and isSpecial(substr, window):
                    visited.add(substr)

                    # check if substr appears at least 3 times
                    count = 0
                    for i in range(n - window + 1):
                        if s[i:].startswith(substr):
                            count += 1

                        # if three appearances, update `spec_substr`
                        if count == 3 and len(substr) > len(spec_substr):
                            spec_substr = substr
                            break

            # update window
            window += 1
    
        return len(spec_substr) if spec_substr else -1