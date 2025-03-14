/*
    [MEDIUM]
    380. Insert Delete GetRandom O(1)

    Concepts:
    - design
    - hash table

    Stats:
        Runtime | 40 ms     [Beats 78.88%]
        Memory  | 112.96 MB [Beats 87.56%]
*/

class RandomizedSet {
public:
    std::unordered_map<int, int> map = {};
    std::vector<int> vec = {};

    RandomizedSet() {}
    
    bool insert(int val) {
        if (map.find(val) == map.end()) {
            map.insert({{val, vec.size()}});
            vec.push_back(val);
            return true;
        }
        return false;
    }
    
    bool remove(int val) {
        if (map.find(val) != map.end()) {
            // since erase is O(n), swap val with last
            // value in vec, then pop from back in O(1)
            int last_val = vec.back();
            // update value
            vec[map[val]] = vec.back();
            vec.pop_back();
            // update index
            map[last_val] = map[val];
            map.erase(val);
            return true;
        }
        return false;
    }
    
    int getRandom() {
        return vec[rand() % vec.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */