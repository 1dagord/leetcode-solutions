/*
    [EASY]
    108. Convert Sorted Array to Binary Search Tree

    Concepts:
    - binary search tree
    - divide and conquer

    Stats:
        Runtime | 4 ms      [Beats 35.67%]
        Memory  | 28.88 MB  [Beats 6.24%]
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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        std::function<TreeNode*(std::vector<int>)> createSubtree;
        createSubtree = [&](std::vector<int> arr){
            int n = arr.size();
            int mid_ind = n / 2;

            TreeNode* curr = new TreeNode(arr[mid_ind]);

            if (mid_ind > 0)
                curr->left = createSubtree(
                    std::vector<int>{arr.begin(), arr.begin() + mid_ind}
                );
            if (mid_ind + 1 < n)
                curr->right = createSubtree(
                    std::vector<int>{arr.begin() + mid_ind + 1, arr.end()}
                );

            return curr;
        };

        return createSubtree(nums);
    }
};