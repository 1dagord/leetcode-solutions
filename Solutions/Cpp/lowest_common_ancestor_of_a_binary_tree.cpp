/*
    [MEDIUM]
    236. Lowest Common Ancestor of a Binary Tree

    Concepts:
    - binary tree
    - depth-first search

    Stats:
        Runtime | 12 ms     [Beats 63.97%]
        Memory  | 17.27 MB  [Beats 88.76%]
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // leaf reached or empty tree
        if (!root)
            return nullptr;

        // if p or q found...
        if (root == p || root == q)
            return root;

        // recursively search left and right subtrees
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);

        if (left && right)
            return root;

        return (left) ? (left) : (right);
    }
};