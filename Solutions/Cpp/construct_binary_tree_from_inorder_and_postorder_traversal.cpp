/*
    [MEDIUM]
    106. Construct Binary Tree from Inorder and Postorder Traversal

    Concepts:
    - binary tree
    - divide and conquer

    Stats:
        Runtime | 24 ms     [Beats 6.69%]
        Memory  | 70.05 MB  [Beats 5.05%]
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
    TreeNode* construct(std::vector<int> iot, std::vector<int> pot) {
        if (iot.empty() || pot.empty())
            return nullptr;

        TreeNode* root = new TreeNode(pot.back());

        // index of root in pot
        auto it = std::find(iot.begin(), iot.end(), pot.back());
        int idx = (it != iot.end()) ? (std::distance(iot.begin(), it)) : (-1);

        // iot: pass left subarray excluding current value
        // pot: pass nodes before and including next root
        root->left = construct(
            std::vector<int>{iot.begin(), iot.begin() + idx},
            std::vector<int>{pot.begin(), pot.begin() + idx}
        );

        // iot: pass right subarray excluding current value
        // pot: pass node between left root and current root; exclusive
        root->right = construct(
            std::vector<int>{iot.begin() + idx + 1, iot.end()},
            std::vector<int>{pot.begin() + idx, pot.end() - 1}
        );

        return root;
    }

    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return construct(inorder, postorder);
    }
};