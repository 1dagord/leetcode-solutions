"""
    [HARD]
    68. Text Justification

    Concepts:
    - string
    - simulation

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.76     [Beats 80.24%]
"""

class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        """
            1) Store lines in list
            2) Add words to line until word length > line length
            3) Join words by adding up lengths, subtracting total
                letter length by max_width, then floor-dividing
                by number of words
        """
        lines = []
        line = []
        words_in_line = 0
        num_letters = 0

        # split words up into lines
        for word in words:
            line_len = len(line)
            word_len = len(word)

            if (words_in_line - 1) + num_letters + word_len < max_width:
                words_in_line += 1
                num_letters += word_len
                line.append(word)
            else:
                lines.append(line)
                words_in_line = 1
                num_letters = word_len
                line = [word]

        if line:
            lines.append(line)

        # add spaces as necessary
        for i, wrds in enumerate(lines):
            num_letters = sum([len(word) for word in wrds])
            num_spaces = max_width - num_letters
            num_gaps = len(wrds) - 1

            # store number of spaces needed to fill gaps
            gaps = []
            while num_gaps:
                space = math.ceil(num_spaces / num_gaps)
                gaps.append(space)

                num_spaces -= space
                num_gaps -= 1

            # different logic for last line
            res = ""
            if i == len(lines) - 1:
                for j in range(len(wrds)-1):
                    res += wrds[j] + " "
            else:
                for j in range(len(wrds)-1):
                    res += wrds[j] + " "*gaps[j]

            res += wrds[-1]
            
            # pad zeroes if needed
            res = res + " "*(max_width - len(res))
            lines[i] = res

        return lines