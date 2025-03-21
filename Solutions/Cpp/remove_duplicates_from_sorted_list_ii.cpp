/*
    [MEDIUM]
    82. Remove Duplicates from Sorted List II

    Concepts:
    - linked list

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 17.26 MB  [Beats 7.52%]
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
    ListNode* deleteDuplicates(ListNode* head) {
        std::unordered_map<int, ListNode*> val_to_node = {};
        std::map<int, int> counter = {};
        ListNode* curr = head;

        while (curr != nullptr) {
            if (!val_to_node.contains(curr->val))
                val_to_node[curr->val] = curr;
            counter[curr->val]++;

            curr = curr->next;
        }

        curr = new ListNode(-1, head);
        ListNode* new_head = curr;
        for (const auto [val, count] : counter) {
            if (count == 1) {
                curr->next = val_to_node[val];
                curr = curr->next;
            }
        }

        curr->next = nullptr;
        return new_head->next;
    }
};