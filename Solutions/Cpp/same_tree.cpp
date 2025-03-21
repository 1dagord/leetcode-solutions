/*
    [EASY]
    100. Same Tree

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 13.03 MB  [Beats 14.69%]
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        std::function<bool(TreeNode*, TreeNode*)> bfs;

        bfs = [](TreeNode* root1, TreeNode* root2){
            std::deque<TreeNode*> queue1 = {root1};
            std::deque<TreeNode*> queue2 = {root2};
            TreeNode* curr1;
            TreeNode* curr2;
            int n1, n2;

            while (!queue1.empty() && !queue2.empty()) {
                n1 = queue1.size();
                n2 = queue2.size();

                if (n1 != n2)
                    return false;
            
                for (int _ = 0; _ < n1; _++) {
                    curr1 = queue1.front();
                    curr2 = queue2.front();

                    queue1.pop_front();
                    queue2.pop_front();

                    if (
                        (curr1 != nullptr && curr2 == nullptr) ||
                        (curr2 != nullptr && curr1 == nullptr)
                    ) {
                        return false;
                    } else if (curr1 != nullptr && curr2 != nullptr) {
                        if (curr1->val != curr2->val)
                            return false;
                    }

                    if (curr1 != nullptr) {
                        queue1.push_back(curr1->left);
                        queue1.push_back(curr1->right);
                    }
                    if (curr2 != nullptr) {
                        queue2.push_back(curr2->left);
                        queue2.push_back(curr2->right);
                    }
                }
            }

            return true;
        };

        return bfs(p, q);
    }
};