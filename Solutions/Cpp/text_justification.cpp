/*
    [HARD]
    68. Text Justification

    Concepts:
    - string
    - simulation

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 10.95 MB  [Beats 6.83%]
*/

class Solution {
public:
    vector<string> fullJustify(vector<string>& words, short max_width) {
        /*
            1) Store lines in list
            2) Add words to line until word length > line length
            3) Join words by adding up lengths, subtracting total
                letter length by max_width, then floor-dividing
                by number of words
        */
        std::vector<std::vector<std::string>> lines = {};
        std::vector<std::string> line = {};
        std::vector<float> gaps = {};
        short words_in_line = 0;
        short num_letters = 0;
        short line_len, word_len, num_spaces, num_gaps;
        float space;
        std::string res = "";
        std::vector<std::string> ans = {};

        // split words up into lines
        for (const std::string word : words) {
            line_len = line.size();
            word_len = word.size();

            if ((words_in_line - 1) + num_letters + word_len < max_width) {
                words_in_line++;
                num_letters += word_len;
                line.push_back(word);
            }
            else {
                lines.push_back(line);
                words_in_line = 1;
                num_letters = word_len;
                line = {word};
            }
        }

        if (!line.empty())
            lines.push_back(line);

        // add spaces as necessary
        for (short i = 0; i < lines.size(); i++) {
            num_letters = std::accumulate(
                lines[i].begin()
                , lines[i].end()
                , 0
                , [](short len_sum, const std::string& str) {
                    return len_sum + str.length();
                }
            );

            num_spaces = max_width - num_letters;
            num_gaps = lines[i].size() - 1;

            // store number of spaces needed to fill gaps
            gaps.clear();
            while (num_gaps) {
                space = std::ceil(((float)num_spaces) / ((float)num_gaps));
                gaps.push_back(space);

                num_spaces -= space;
                num_gaps--;
            }

            // different logic for last line
            res.clear();
            if (i == lines.size() - 1) {
                for (short j = 0; j < lines[i].size() - 1; j++)
                    res += lines[i][j] + " ";
            } else {
                for (short j = 0; j < lines[i].size() - 1; j++) {
                    res += lines[i][j];
                    for (short _ = 0; _ < gaps[j]; _++)
                        res += " ";
                }
            }

            res += lines[i].back();
            
            // pad zeroes if needed
            const int remaining_spaces = max_width - res.size();
            for (short j = 0; j < remaining_spaces; j++)
                res += " ";
            ans.push_back(res);
        }

        return ans;
    }
};