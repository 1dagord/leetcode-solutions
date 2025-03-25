/*
    [MEDIUM]
    105. Construct Binary Tree from Preorder and Inorder Traversal

    Concepts:
    - binary tree
    - divide and conquer

    Stats:
        Runtime | 23 ms     [Beats 10.85%]
        Memory  | 74.88 MB  [Beats 6.57%]
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
    TreeNode* construct(std::vector<int> prot, std::vector<int> iot) {
        if (prot.empty() || iot.empty())
            return nullptr;

        TreeNode* root = new TreeNode(prot.front());

        // index of root in iot
        auto it = std::find(iot.begin(), iot.end(), prot.front());
        int idx = (it != iot.end()) ? (std::distance(iot.begin(), it)) : (-1);

        // prot: pass only node following root
        // iot: pass left subarray excluding current value
        root->left = construct(
            std::vector<int>{prot.begin() + 1, prot.begin() + idx + 1},
            std::vector<int>{iot.begin(), iot.begin() + idx}
        );

        // prot: pass all nodes following root
        // iot: pass right subarray excluding current value
        root->right = construct(
            std::vector<int>{prot.begin() + idx + 1, prot.end()},
            std::vector<int>{iot.begin() + idx + 1, iot.end()}
        );

        return root;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return construct(preorder, inorder);
    }
};