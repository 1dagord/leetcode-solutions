/*
    [MEDIUM]
    133. Clone Graph

    Concepts:
    - graph
    - breadth-first search

    Stats:
        Runtime | 3 ms      [Beats 67.71%]
        Memory  | 12.15 MB  [Beats 47.01%]
*/

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node || node->neighbors.empty())
            return (node) ? (new Node(node->val)) : (nullptr);

        std::unordered_map<Node*, std::unordered_set<Node*>> adj = {};

        // explore graph and update adjacency list
        std::queue<Node*> q;
        q.push(node);
        int len_q;
        Node* curr;

        while (!q.empty()) {
            len_q = q.size();

            for (int _ = 0; _ < len_q; _++) {
                curr = q.front();
                q.pop();

                for (Node* n : curr->neighbors) {
                    // if neighbor not explored...
                    if (adj[n].empty())
                        q.push(n);

                    adj[curr].insert(n);
                }
            }
        }

        // rebuild graph from adjacency list
        std::unordered_map<int, Node*> nodes = {};
        for (auto& [n, _] : adj)
            nodes[n->val] = new Node(n->val);

        for (auto& [nde, nei] : adj) {
            for (Node* nbr : nei)
                nodes[nde->val]->neighbors.push_back(nodes[nbr->val]);
        }

        return nodes[node->val];
    }
};