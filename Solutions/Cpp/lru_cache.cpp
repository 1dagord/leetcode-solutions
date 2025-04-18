/*
    [MEDIUM]
    146. LRU Cache

    Concepts:
    - design
    - hash table
    - linked list

    Stats:
        Runtime | 51 ms     [Beats 95.69%]
        Memory  | 174.82 MB [Beats 57.10%]
*/

class DLLNode {
public:
    int val;
    DLLNode* left;
    DLLNode* right;

    DLLNode(int _val) {
        val = _val;
        left = nullptr;
        right = nullptr;
    }
};

class DoublyLinkedList {
public:
    DLLNode* head;
    DLLNode* tail;
    std::unordered_map<int, DLLNode*> key_to_node;

    DoublyLinkedList() {
        head = new DLLNode(-1);
        tail = nullptr;
        head->right = tail;
        key_to_node = {};
    }

    void insert(int key) {
        DLLNode* node = new DLLNode(key);

        if (tail) {
            tail->right = node;
            node->left = tail;
        } else {
            head->right = node;
            node->left = head;
        }
        // reset tail to current node
        tail = node;
        // bind key to DLLNode pointer
        key_to_node[key] = node;
    }

    DLLNode* splice(int key) {
        /*
            Splices out node from doubly linked list
        */
        DLLNode* node = key_to_node[key];

        if (node == tail) {
            tail = tail->left;
            return node;
        }

        node->left->right = node->right;
        node->right->left = node->left;
        return node;
    }

    void update(int key) {
        /*
            Update recency of node after use
        */
        // splice out node
        DLLNode* node = splice(key);
        
        // append node to end of DLL
        tail->right = node;
        node->left = tail;
        node->right = nullptr;
        // set appended node as tail
        tail = node;
    }
};

class LRUCache {
public:
    int capacity;
    std::unordered_map<int, int> cache;
    DoublyLinkedList dll;

    LRUCache(int _capacity) {
        capacity = _capacity;
        cache = {};
        dll = DoublyLinkedList();
    }
    
    int get(int key) {
        if (cache.contains(key)) {
            dll.update(key);
            return cache[key];
        }
        return -1;
    }
    
    void put(int key, int value) {
        if (cache.contains(key))
            dll.update(key);
        else
            dll.insert(key);

        // set/update key-value pair
        cache[key] = value;

        if (cache.size() > capacity) {
            // evict lru
            int lru = (dll.head->val == -1) ? (dll.head->right->val) : (dll.head->val);
            cache.erase(lru);
            // splice out lru
            dll.splice(lru);
            // remove mapping to node
            dll.key_to_node.erase(lru);
        }
    }
};

/**
    * Your LRUCache object will be instantiated and called as such:
    * LRUCache* obj = new LRUCache(capacity);
    * int param_1 = obj->get(key);
    * obj->put(key,value);
    */