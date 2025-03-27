/*
    [MEDIUM]
    124. Binary Tree Maximum Path Sum

    Concepts:
    - binary tree
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 27.82 MB  [Beats 77.25%]
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
    int max_path_sum = std::numeric_limits<int>::min();

    int dfs(TreeNode* curr) {
        if (curr == nullptr)
            return 0;

        // maxes if not splitting at curr
        int left = std::max(0, dfs(curr->left));
        int right = std::max(0, dfs(curr->right));

        // compare with path made from subtrees
        max_path_sum = std::max(max_path_sum, left + right + curr->val);

        // max if splitting at curr
        return std::max(left, right) + curr->val;
    }

    int maxPathSum(TreeNode* root) {
        dfs(root);
        return max_path_sum;
    }
};