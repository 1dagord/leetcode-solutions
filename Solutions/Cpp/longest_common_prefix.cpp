/*
    [EASY]
    14. Longest Common Prefix

    Concepts:
    - string
    - trie

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 12.36 MB  [Beats 12.72%]
*/

class TrieNode {
public:
    std::unordered_map<char, TrieNode*> nodes;
    bool is_leaf;

    TrieNode() :
        is_leaf(false),
        nodes({})
    {}

    void insert(const string& str) {
        TrieNode* curr = this;

        for (char c : str) {
            if (!curr->nodes.contains(c))
                curr->nodes[c] = new TrieNode();

            curr = curr->nodes[c];
        }

        curr->is_leaf = true;
    }
};

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        TrieNode* curr = new TrieNode();
        std::string prefix = "";

        for (std::string word : strs)
            curr->insert(word);

        for (char c : strs[0]) {
            if (curr->nodes.size() > 1 || curr->is_leaf)
                break;

            prefix += c;
            curr = curr->nodes[c];
        }

        return prefix;
    }
};