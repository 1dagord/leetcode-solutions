/*
    [MEDIUM]
    211. Design Add and Search Words Data Structure

    Concepts:
    - design
    - trie
    - depth-first search

    Stats:
        Runtime | 778 ms    [Beats 13.68%]
        Memory  | 549.47 MB [Beats 72.89%]
*/

class TrieNode {
public:
    std::unordered_map<char, TrieNode*> nodes;
    bool is_leaf;

    TrieNode() {
        nodes = {};
        is_leaf = false;
    }
};

class WordDictionary {
public:
    TrieNode* root;

    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* curr = this->root;

        for (const char c : word) {
            if (!curr->nodes.contains(c))
                curr->nodes[c] = new TrieNode();
            curr = curr->nodes[c];
        }
        curr->is_leaf = true;
    }
    
    bool search(string target) {
        std::function<bool(TrieNode*, int)> dfs;

        dfs = [&](TrieNode* curr, int idx){
            if (!curr)
                return false;

            // if entire target searched...
            if (idx == target.size())
                return curr->is_leaf;

            // if leaf reached before entire target searched...
            if (curr->nodes.contains(target[idx]))
                return dfs(curr->nodes[target[idx]], idx + 1);

            if (target[idx] == '.') {
                for (const auto& [c, node] : curr->nodes) {
                    if (curr && dfs(node, idx + 1))
                        return true;
                }
            }

            return false;
        };

        return dfs(this->root, 0);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */