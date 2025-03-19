/*
    [MEDIUM]
    92. Reverse Linked List II

    Concepts:
    - linked list

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 11.14 MB  [Beats 72.55%]
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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        /*
            Use LIFO properties of stack to reverse node
            and splice together reversed portion with
            prepended and appended list
        */
        ListNode* dummy = new ListNode(0, head);
        ListNode* pre = dummy;
        ListNode* prev = dummy;
        ListNode* curr = dummy;
        ListNode* post = head;

        ListNode* res = dummy;

        if (left == right)
            return head;

        // shift in curr and post pointers
        while (right - left) {
            curr = curr->next;
            post = post->next;
            right--;
        }

        while (left) {
            if (left > 1)
                pre = pre->next;

            prev = prev->next;
            curr = curr->next;
            post = post->next;

            left--;
        }

        // add nodes to stack
        std::vector<ListNode*> middle_nodes = {};

        // get all nodes in between
        ListNode* temp = prev;
        while (temp != post) {
            middle_nodes.push_back(temp);
            temp = temp->next;
        }

        // pop nodes off stack and append to list
        while (!middle_nodes.empty()) {
            pre->next = middle_nodes.back();
            middle_nodes.pop_back();
            pre = pre->next;
        }

        pre->next = (post != nullptr) ? (post) : (nullptr);

        return res->next;
    }
};