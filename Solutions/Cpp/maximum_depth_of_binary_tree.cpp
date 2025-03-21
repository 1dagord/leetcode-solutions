/*
    [EASY]
    104. Maximum Depth of Binary Tree

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 19.07 MB  [Beats 45.04%]
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
    int maxDepth(TreeNode* root) {
        if (root == nullptr)
            return 0;

        int depth_count = 0;
        int n;
        std::deque<TreeNode*> dq = {root};
        TreeNode* node;

        while (!dq.empty()) {
            n = dq.size();
            depth_count++;

            for (int _ = 0; _ < n; _++) {
                node = dq.front();
                dq.pop_front();

                if (node->left != nullptr)
                    dq.push_back(node->left);
                if (node->right != nullptr)
                    dq.push_back(node->right);
            }
        }

        return depth_count;
    }
};