/*
    [EASY]
    226. Invert Binary Tree

    Concepts:
    - binary tree
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 12.36 MB  [Beats 63.59%]
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
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }
        
        swapTrees(root);

        invertTree(root->left);
        invertTree(root->right);
        return root;
    }

    void swapTrees(TreeNode* root) {
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        return;
    }
};