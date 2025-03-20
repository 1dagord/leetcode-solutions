/*
    [HARD]
    25. Reverse Nodes in k-Group

    Concepts:
    - linked list
    - recursion

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.46 MB  [Beats 5.87%]
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        int idx = 0;
        std::vector<ListNode*> nodes = {};
        ListNode* curr = head;

        // build group
        while (curr != nullptr && idx != k) {
            nodes.push_back(curr);
            idx++;
            curr = curr->next;
        }

        // do not reverse if < k nodes left
        if (nodes.size() != k)
            return head;

        // reverse nodes
        for (int i = 1; i < k; i++)
            nodes[i]->next = nodes[i-1];

        // continue iteration
        nodes[0]->next = reverseKGroup(curr, k);

        return nodes.back();
    }
};