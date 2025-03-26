/*
    [MEDIUM]
    114. Flatten Binary Tree to Linked List

    Concepts:
    - binary tree
    - linked list
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.88 MB  [Beats 7.84%]
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
class Solution {
public:
    std::vector<TreeNode*> prot = {}; // pre-order traversal

    void dfs(TreeNode* curr) {
        if (curr == nullptr)
            return;

        prot.push_back(curr);

        dfs(curr->left);
        dfs(curr->right);
    };

    void flatten(TreeNode* root) {
        if (root == nullptr)
            return;
            
        dfs(root);

        for (int i = 0; i < prot.size() - 1; i++) {
            prot[i]->left = nullptr;
            prot[i]->right = prot[i+1];
        }
    }
};