/*
    [HARD]
    23. Merge k Sorted Lists

    Concepts:
    - heap/priority queue
    - linked list

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 18.27 MB  [Beats 89.60%]
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        /*
            Keep a priority queue with all heads of linked lists
            Pop off heap and push next value until no values left
        */
        ListNode* dummy = new ListNode();
        auto compare = [](const ListNode* a, const ListNode* b){ return a->val > b->val; };
        std::priority_queue<ListNode*, std::vector<ListNode*>, decltype(compare)> heap;

        // append all head nodes to heap
        for (ListNode* head : lists)
            if (head)
                heap.push(head);

        ListNode* head = dummy;
        while (!heap.empty()) {
            ListNode* curr = heap.top(); heap.pop();
            ListNode* nxt = curr->next;

            // push next node to heap
            if (nxt)
                heap.push(nxt);

            head->next = curr;
            head = head->next;
        }

        return dummy->next;
    }
};