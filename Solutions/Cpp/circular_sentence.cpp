/*
    [EASY]
    2490. Circular Sentence

    Concepts:
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 9.41 MB   [Beats 9.08%]
 */

class Solution {
public:
    bool isCircularSentence(string sentence) {
        vector<string> words = {};

        while (sentence.find(" ") != string::npos) {
            words.push_back(sentence.substr(0, sentence.find(" ")));
            sentence = sentence.substr(sentence.find(" ")+1);
        }
        words.push_back(sentence);

        for (int i = 0; i < words.size() - 1; i++) {
            string curr_word = words[i];
            string next_word = words[i+1];
            // check last char of curr and first of next
            if (curr_word.at(curr_word.size()-1) != next_word.at(0)) {
                return false;
            }
        }

        string first_word = words.at(0);
        string last_word = words.at(words.size()-1);
    
        return first_word.at(0) == last_word.at(last_word.size()-1);
    }
};