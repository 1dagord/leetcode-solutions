/*
    [EASY]
    112. Path Sum

    Concepts:
    - binary tree
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 21.52 MB  [Beats 34.61%]
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
    int target;

    bool dfs(TreeNode* curr, int path_sum) {
        bool outcome = false;

        if (curr->left == nullptr && curr->right == nullptr && path_sum == target)
            return true;

        if (curr->left != nullptr)
            outcome |= dfs(curr->left, path_sum + curr->left->val);

        if (curr->right != nullptr)
            outcome |= dfs(curr->right, path_sum + curr->right->val);

        return outcome;
    }

    bool hasPathSum(TreeNode* root, int targetSum) {
        target = targetSum;
        return (root != nullptr) ? (dfs(root, root->val)) : (false);
    }
};