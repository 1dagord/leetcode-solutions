/*
    [MEDIUM]
    230. Kth Smallest Element in a BST

    Concepts:
    - binary search tree
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 24.54 MB  [Beats 28.93%]
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

    void dfs(TreeNode* curr) {
        if (!curr)
            return;

        dfs(curr->left);
        iot.push_back(curr->val);
        dfs(curr->right);
    }

    int kthSmallest(TreeNode* root, int k) {
        dfs(root);
        return iot[k - 1];    
    }
};