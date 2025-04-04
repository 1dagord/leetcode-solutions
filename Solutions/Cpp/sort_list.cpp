/*
    [MEDIUM]
    148. Sort List

    Concepts:
    - linked list
    - sorting

    Stats:
        Runtime | 53 ms     [Beats 23.27%]
        Memory  | 75.73 MB  [Beats 21.02%]
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
    ListNode* findMiddle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head->next;

        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
        }

        return slow;
    }

    ListNode* merge(ListNode* left, ListNode* right) {
        ListNode* dummy = new ListNode(-1);
        ListNode* curr = dummy;

        while (left && right) {
            if (left->val < right->val) {
                curr->next = left;
                curr = left;
                left = left->next;
            } else {
                curr->next = right;
                curr = right;
                right = right->next;
            }
        }

        curr->next = (left) ? (left) : (right);

        return dummy->next;
    }

    ListNode* mergeSort(ListNode* head) {
        if (!head || !head->next)
            return head;

        ListNode* middle = findMiddle(head);
        ListNode* left_head = head;
        ListNode* right_head = middle->next;
        middle->next = nullptr;

        ListNode* left = mergeSort(left_head);
        ListNode* right = mergeSort(right_head);

        return merge(left, right);
    }
    
    ListNode* sortList(ListNode* head) {
        return mergeSort(head);
    }
};