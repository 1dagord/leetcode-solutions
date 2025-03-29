/*
    [HARD]
    127. Word Ladder

    Concepts:
    - string
    - hash table
    - breadth-first search

    Stats:
        Runtime | 1344 ms   [Beats 7.65%]
        Memory  | 41.56 MB  [Beats 10.88%]
*/

class Solution {
public:
    int ladderLength(string begin_word, string end_word, vector<string>& word_list) {
        std::unordered_set<std::string> word_set(word_list.begin(), word_list.end());
        int int_a = int('a');
        
        if (!word_set.contains(end_word))
            return 0;

        // bfs
        std::queue<std::pair<std::string, int>> q;
        q.push({begin_word, 1});
        std::unordered_set<std::string> visited = {};

        int len_q, count;
        std::string curr, new_word, letters;
        char c;

        while (!q.empty()) {
            len_q = q.size();

            for (int _ = 0; _ < len_q; _++) {
                auto [curr, count] = q.front();
                q.pop();
                visited.insert(curr);

                if (curr == end_word)
                    return count;

                letters = curr;

                for (int i = 0; i < letters.size(); i++) {
                    c = letters[i];
                    for (int j = 0; j < 26; j++) {
                        letters[i] = char(((int_a + j) % 26) + int_a);

                        if (word_set.contains(letters) && !visited.contains(letters))
                            q.push({letters, count + 1});
                    }

                    // reset letters
                    letters[i] = c;
                }
            }
        }

        return 0;
    }
};