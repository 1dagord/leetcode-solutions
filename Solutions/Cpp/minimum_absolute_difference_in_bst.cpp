/*
    [MEDIUM]
    530. Minimum Absolute Difference in BST

    Concepts:
    - binary search tree
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 24.17 MB  [Beats 86.91%]
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
    vector<int> iot;
    void dfs(TreeNode* curr){
        if (curr->left != nullptr) dfs(curr->left);
        iot.push_back(curr->val);
        if (curr->right != nullptr) dfs(curr->right);
    }
    
    int getMinimumDifference(TreeNode* root) {
        dfs(root);
        int min_diff = std::numeric_limits<int>::max();

        for (int i = 1; i < iot.size(); i++) {
            min_diff = std::min(min_diff, std::abs(iot[i] - iot[i-1]));
        }
        
        return min_diff;
    }
};