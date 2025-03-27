/*
    [MEDIUM]
    199. Binary Tree Right Side View

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 15.14 MB  [Beats 26.19%]
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
    vector<int> rightSideView(TreeNode* root) {
        // level order, but only keep last element
        std::vector<int> levels = {};

        if (!root)
            return levels;

        std::queue<TreeNode*> q;
        q.push(root);
        TreeNode* curr;
        int n;

        while (!q.empty()) {
            n = q.size();

            for (int i = 0; i < n; i++) {
                curr = q.front();
                q.pop();

                if (curr->left)
                    q.push(curr->left);
                if (curr->right)
                    q.push(curr->right);

                if (i == n - 1)
                    levels.push_back(curr->val);
            }
        }

        return levels;
    }
};