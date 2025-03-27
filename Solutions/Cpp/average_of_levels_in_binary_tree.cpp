/*
    [EASY]
    637. Average of Levels in Binary Tree

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 23.93 MB  [Beats 27.96%]
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
    vector<double> averageOfLevels(TreeNode* root) {
        std::vector<double> averages = {};

        std::queue<TreeNode*> q;
        q.push(root);
        double level_sum;
        int level_len;
        TreeNode* curr;

        while (!q.empty()) {
            level_len = q.size();
            level_sum = 0.0;

            for (int _ = 0; _ < level_len; _++) {
                curr = q.front();
                q.pop();

                level_sum += curr->val;

                if (curr->left)
                    q.push(curr->left);
                if (curr->right)
                    q.push(curr->right);
            }

            averages.push_back(level_sum / level_len);
        }

        return averages;
    }
};