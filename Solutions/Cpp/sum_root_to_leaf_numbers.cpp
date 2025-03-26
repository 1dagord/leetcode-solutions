/*
    [MEDIUM]
    129. Sum Root to Leaf Numbers

    Concepts:
    - binary tree
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 14.83 MB  [Beats 5.23%]
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
    int rtl_sum = 0;
    
    int convert(std::vector<int> l) {
        int output = 0;
        int n = l.size();
        for (int i = 0; i < n; i++)
            output += l[n-1-i] * std::pow(10, i);
        return output;
    }

    void dfs(TreeNode* curr, std::vector<int> path) {
        if (curr->left != nullptr) {
            path.push_back(curr->left->val);
            dfs(curr->left, path);
            path.pop_back();
        }
    
        if (curr->right != nullptr) {
            path.push_back(curr->right->val);
            dfs(curr->right, path);
            path.pop_back();
        }

        if (curr->left == nullptr && curr->right == nullptr)
            rtl_sum += convert(path);
    }

    int sumNumbers(TreeNode* root) {
        dfs(root, std::vector<int>{root->val});
        return rtl_sum;
    }
};