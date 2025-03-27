/*
    [EASY]
    222. Count Complete Tree Nodes

    Concepts:
    - binary tree
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 31.19 MB  [Beats 94.41%]
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
    int count = 0;

    void dfs(TreeNode* curr) {
        if (curr == nullptr)
            return;
        
        dfs(curr->left);
        count++;
        dfs(curr->right);
    }

    int countNodes(TreeNode* root) {
        dfs(root);
        return count;
    }
};