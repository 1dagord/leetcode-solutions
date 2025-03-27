/*
    [MEDIUM]
    103. Binary Tree Zigzag Level Order Traversal

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 15.10 MB  [Beats 76.77%]
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        std::vector<std::vector<int>> levels = {};
        std::vector<int> level = {};

        if (!root)
            return levels;

        std::queue<TreeNode*> q;
        q.push(root);
        int n;
        bool is_forward = true;
        TreeNode* curr;

        while (!q.empty()) {
            n = q.size();
            level.clear();

            for (int _ = 0; _ < n; _++) {
                curr = q.front();
                q.pop();
                level.push_back(curr->val);

                if (curr->left)
                    q.push(curr->left);
                if (curr->right)
                    q.push(curr->right);
            }

            if (!is_forward)
                std::reverse(level.begin(), level.end());

            is_forward = !is_forward;
            levels.push_back(level);
        }

        return levels;
    }
};