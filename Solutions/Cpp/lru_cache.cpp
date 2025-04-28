/*
    [MEDIUM]
    146. LRU Cache

    Concepts:
    - design
    - hash table
    - linked list

    Stats:
        Runtime | 46 ms     [Beats 96.50%]
        Memory  | 173.24 MB [Beats 62.89%]
*/

class LRUCache {
    public:
        int capacity;
        std::unordered_map<int, std::list<std::pair<int, int>>::iterator> cache;
        std::list<std::pair<int, int>> dll;
    
        LRUCache(int _capacity) {
            capacity = _capacity;
            cache = {};
            dll = {};
        }
        
        int get(int key) {
            if (cache.contains(key)) {
                dll.splice(dll.begin(), dll, cache[key]);
                return cache[key]->second;
            }
            return -1;
        }
        
        void put(int key, int value) {
            if (cache.contains(key)) {
                dll.splice(dll.begin(), dll, cache[key]);
                cache[key]->second = value;
                return;
            }
    
            dll.push_front({key, value});
            cache.insert({key, dll.begin()});
    
            if (dll.size() > capacity) {
                int lru = dll.back().first;
                dll.pop_back();
                cache.erase(lru);
            }
        }
    };
    
    /**
     * Your LRUCache object will be instantiated and called as such:
     * LRUCache* obj = new LRUCache(capacity);
     * int param_1 = obj->get(key);
     * obj->put(key,value);
     */