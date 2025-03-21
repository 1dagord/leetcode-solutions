/*
    [EASY]
    101. Symmetric Tree

    Concepts:
    - binary tree
    - depth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 19.04 MB  [Beats 5.90%]
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
    bool isSymmetric(TreeNode* root) {
        std::function<bool(TreeNode*, TreeNode*)> dfs;

        dfs = [&](TreeNode* node1, TreeNode* node2){
            if (node1 == nullptr && node2 == nullptr)
                return true;
            if (node1 == nullptr || node2 == nullptr)
                return false;

            return (
                node1->val == node2->val &&
                dfs(node1->left, node2->right) &&
                dfs(node1->right, node2->left)
            );
        };

        return dfs(root->left, root->right);
    }
};