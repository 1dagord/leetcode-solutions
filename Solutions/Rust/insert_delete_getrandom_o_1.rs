/*
    [MEDIUM]
    380. Insert Delete GetRandom O(1)

    Concepts:
    - design
    - hash table

    Stats:
        Runtime | 41 ms     [Beats 59.43%]
        Memory  | 29.95 MB  [Beats 89.62%]
*/
use std::collections::HashMap;
use rand::Rng;

struct RandomizedSet {
    map: HashMap::<i32, usize>,
    vec: Vec<i32>,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {
    fn new() -> Self {
        return RandomizedSet{
            map: HashMap::new(),
            vec: Vec::new(),
        };
    }
    
    fn insert(&mut self, val: i32) -> bool {
        if !self.map.contains_key(&val) {
            self.map.insert(val, self.vec.len());
            self.vec.push(val);
            return true;
        }
        return false;
    }
    
    fn remove(&mut self, val: i32) -> bool {
        if self.map.contains_key(&val) {
            let last_val: i32 = *self.vec.last().unwrap();
            self.vec[self.map[&val]] = last_val;
            self.vec.pop();
            self.map.insert(last_val, self.map[&val]);
            self.map.remove(&val);
            return true;
        }
        return false;
    }
    
    fn get_random(&self) -> i32 {
        return self.vec[rand::thread_rng().gen_range(0..self.vec.len())];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */