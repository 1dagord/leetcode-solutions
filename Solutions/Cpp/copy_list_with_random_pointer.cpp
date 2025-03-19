/*
    [MEDIUM]
    138. Copy List with Random Pointer

    Concepts:
    - linked list
    - hash table

    Stats:
        Runtime | 9 ms      [Beats 21.24%]
        Memory  | 15.15 MB  [Beats 50.27%]
*/

/*
// Definition for a Node.
class Node {
public:
int val;
Node* next;
Node* random;

Node(int _val) {
    val = _val;
    next = NULL;
    random = NULL;
}
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr)
            return nullptr;

        // Node_Object -> node.val
        std::unordered_map<Node*, Node*> orig_to_cpy = {};
        Node* curr;

        // associate each node object with a
        // new node of same value
        curr = head;
        while (curr != nullptr) {
            orig_to_cpy[curr] = new Node(curr->val);
            curr = curr->next;
        }

        // link all new nodes together using
        // `next` and `random` of old nodes
        curr = head;
        while (curr != nullptr) {
            orig_to_cpy[curr]->next = (orig_to_cpy.contains(curr->next)) ?
            (orig_to_cpy[curr->next]) : (nullptr);
            orig_to_cpy[curr]->random = (orig_to_cpy.contains(curr->random)) ?
            (orig_to_cpy[curr->random]) : (nullptr);

            curr = curr->next;
        }

        // return cop of new list
        return orig_to_cpy[head];
    }
};