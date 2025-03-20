/*
    [MEDIUM]
    19. Remove Nth Node From End of List

    Concepts:
    - linked list
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 15.10 MB  [Beats 25.11%]
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* curr = head;

        // iterate n nodes into list
        while (n--)
            curr = curr->next;

        // prepend dummy node so prev->next is node to delete
        ListNode* dummy = new ListNode(-1, head);
        ListNode* prev = dummy;

        // put prev into position
        while (curr != nullptr) {
            prev = prev->next;
            curr = curr->next;
        }

        // if already at end of list, remove first element
        if (prev == dummy)
            return head->next;

        // splice out node
        prev->next = prev->next->next;

        return head;
    }
};