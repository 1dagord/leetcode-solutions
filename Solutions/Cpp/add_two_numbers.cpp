/*
    [MEDIUM]
    2. Add Two Numbers

    Concepts:
    - linked list
    - math

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 77.23 MB  [Beats 12.25%]
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        int num;
        ListNode* res = new ListNode(-1);
        ListNode* head = res;

        while (l1 != nullptr && l2 != nullptr) {
            num = l1->val + l2->val + carry;
            carry = (num > 9) ? (1) : (0);

            res->next = new ListNode(num % 10);
            res = res->next;

            l1 = l1->next;
            l2 = l2->next;
        }

        while (l1 != nullptr) {
            num = l1->val + carry;
            carry = (num > 9) ? (1) : (0);

            res->next = new ListNode(num % 10);
            res = res->next;

            l1 = l1->next;
        }

        while (l2 != nullptr) {
            num = l2->val + carry;
            carry = (num > 9) ? (1) : (0);

            res->next = new ListNode(num % 10);
            res = res->next;

            l2 = l2->next;
        }

        res->next = (carry == 1) ? (new ListNode(1)) : (nullptr);

        return head->next;
    }
};