/*
    [MEDIUM]
    117. Populating Next Right Pointers in Each Node II

    Concepts:
    - binary tree
    - breadth-first search

    Stats:
        Runtime | 11 ms     [Beats 45.65%]
        Memory  | 18.91 MB  [Beats 34.02%]
*/

/*
// Definition for a Node.
class Node {
public:
int val;
Node* left;
Node* right;
Node* next;

Node() : val(0), left(NULL), right(NULL), next(NULL) {}

Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

Node(int _val, Node* _left, Node* _right, Node* _next)
    : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if (root == nullptr)
            return root;

        std::queue<Node*> q;
        q.push(root);

        int len_q;
        Node* curr;

        while (!q.empty()) {
            len_q = q.size();

            for (int i = 0; i < len_q; i++) {
                curr = q.front();
                q.pop();

                if (i != len_q - 1)
                    curr->next = q.front();

                if (curr->left != nullptr)
                    q.push(curr->left);

                if (curr->right != nullptr)
                    q.push(curr->right);
            }
        }

        return root;
    }
};