/*
    [MEDIUM]
    86. Partition List

    Concepts:
    - linked list

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 15.02 MB  [Beats 11.39%]
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
    ListNode* partition(ListNode* head, int x) {
        ListNode* lt = new ListNode(-1);
        ListNode* gte = new ListNode(-1);
        ListNode* lt_head = lt;
        ListNode* gte_head = gte;

        ListNode* curr = head;

        while (curr != nullptr) {
            if (curr->val < x) {
                lt->next = curr;
                lt = lt->next;
            } else {
                gte->next = curr;
                gte = gte->next;
            }
            curr = curr->next;
        }

        lt->next = gte_head->next;
        gte->next = nullptr;

        return lt_head->next;
    }
};