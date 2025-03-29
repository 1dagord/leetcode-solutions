/*
    [MEDIUM]
    208. Implement Trie (Prefix Tree)

    Concepts:
    - design
    - hash table
    - string

    Stats:
        Runtime | 41 ms     [Beats 18.39%]
        Memory  | 48.74 MB  [Beats 85.35%]
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

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* curr = this->root;

        for (const char c : word) {
            if (!curr->nodes.contains(c)) {
                // adds each character to nodes
                curr->nodes[c] = new TrieNode();
            }
            curr = curr->nodes[c];
        }

        // once entire word has been added, set to true
        curr->is_leaf = true;
    }
    
    bool search(string word) {
        TrieNode* curr = this->root;

        for (const char c : word) {
            // if any missing letters, return false
            if (!curr->nodes.contains(c))
                return false;

            curr = curr->nodes[c];
        }

        // true only if whole word found
        return curr->is_leaf;
    }
    
    bool startsWith(string prefix) {
        TrieNode* curr = this->root;

        for (const char c : prefix) {
            if (!curr->nodes.contains(c))
                return false;
            
            curr = curr->nodes[c];
        }

        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */