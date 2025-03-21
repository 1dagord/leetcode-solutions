/*
    [HARD]
    30. Substring with Concatenation of All Words

    Concepts:
    - string
    - hash table
    - depth-first search

    Stats:
        Runtime | 397 ms    [Beats 95.63%]
        Memory  | 306.29 MB [Beats 12.86%]
*/

class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        if (std::unordered_set<std::string>{words.begin(), words.end()}.size() == 1) {
            std::string one_word = std::accumulate(words.begin(), words.end(), std::string{});
            words.clear();
            words.push_back(one_word);
        }

        short word_length = words[0].size();
        short all_words_length = word_length * words.size();
        short s_length = s.size();

        std::vector<int> indices = {};
        std::unordered_map<std::string, short> remaining = {};
        for (const std::string word : words)
            remaining[word]++;

        std::function<void(short)> dfs = [&](short idx){
            if (remaining.empty()) {
                indices.push_back(idx - all_words_length);
                return;
            }

            std::string word = s.substr(idx, word_length);
            if (remaining.contains(word)) {
                remaining[word]--;
                if (remaining[word] == 0)
                    remaining.erase(word);

                dfs(idx + word_length);

                remaining[word]++;
            }
        };

        for (short i = 0; i < s_length; i++) {
            if (remaining.contains(s.substr(i, word_length)))
                dfs(i);
        }

        return indices;
    }
};