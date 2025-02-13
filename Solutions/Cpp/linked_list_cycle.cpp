/*
    [EASY]
    141. Linked List Cycle

    Concepts:
    - two pointers
    - linked list

    Stats:
        Runtime | 8 ms      [Beats 81.28%]
        Memory  | 11.71 MB  [Beats 80.04%]
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == NULL || head->next == NULL)
            return false;

        ListNode* tortoise = head;
        ListNode* hare = head;

        while (hare != NULL && hare->next != NULL) {
            tortoise = tortoise->next;
            hare = hare->next->next;

            if (tortoise == hare)
                return true;
        }
        return false;
    }
};