/*
    [MEDIUM]
    61. Rotate List

    Concepts:
    - linked list
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 16.40 MB  [Beats 31.86%]
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
    ListNode* rotateRight(ListNode* head, int k) {
        /*
            1) iterate into list until k == 0 or
                curr.next == None
            2) store new_head.next and set new_head.next = None
            3) set curr.next = head
            4) return new_head
        */
        if (head == nullptr || head->next == nullptr)
            return head;

        // mod k by length to avoid unnecessary work
        int length = 0;
        ListNode* curr = head;
        while (curr != nullptr) {
            length++;
            curr = curr->next;
        }

        k %= length;

        // get new head
        curr = head;
        while (k--) {
            if (curr == nullptr)
                curr = head;
            curr = curr->next;
        }

        // if at end of list, rotation is identical to list
        if (curr == nullptr)
            return head;

        ListNode* new_head = head;

        // iterate to end of array
        while (curr->next != nullptr) {
            curr = curr->next;
            new_head = new_head->next;
        }

        ListNode* next_head;
        if (new_head != curr) {
            // store head value of rotated list
            next_head = new_head->next;
            // set prev value's next to nullptr
            new_head->next = nullptr;
            // point last node back to first
            curr->next = head;
        } else {
            next_head = head;
        }

        return next_head;
    }
};