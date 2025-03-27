/*
    [MEDIUM]
    173. Binary Search Tree Iterator

    Concepts:
    - binary search tree
    - depth-first search

    Stats:
        Runtime | 4 ms      [Beats 54.84%]
        Memory  | 32.15 MB  [Beats 23.51%]
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class BSTIterator {
public:
    int n, idx;
    std::vector<int> iot;

    BSTIterator(TreeNode* root) {
        idx = -1;
        iot = {};
        dfs(root);
        n = iot.size();
    }

    void dfs(TreeNode* curr) {
        if (curr == nullptr)
            return;

        dfs(curr->left);
        iot.push_back(curr->val);
        dfs(curr->right);
    }
    
    int next() {
        return iot.at(++idx);
    }
    
    bool hasNext() {
        if (idx == -1)
            return &iot.front() != nullptr;
        return idx + 1 < n;
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */