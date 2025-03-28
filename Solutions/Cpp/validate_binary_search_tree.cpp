/*
    [MEDIUM]
    98. Validate Binary Search Tree

    Concepts:
    - binary search tree
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 22.20 MB  [Beats 9.62%]
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
    std::vector<int> iot = {};

    bool dfs(TreeNode* curr) {
        if (!curr)
            return true;

        bool outcome = true;

        outcome &= dfs(curr->left);

        if (!iot.empty() && curr->val <= iot.back())
            return false;
        iot.push_back(curr->val);

        outcome &= dfs(curr->right);

        return outcome;
    }

    bool isValidBST(TreeNode* root) {
        return dfs(root);
    }
};