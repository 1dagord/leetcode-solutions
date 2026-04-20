/*
    [EASY]
    14. Longest Common Prefix

    Concepts:
    - string
    - trie

    Stats:
        Runtime | 2 ms      [Beats 7.98%]
        Memory  | 2.21 MB   [Beats 61.66%]
*/
use std::collections::HashMap;

struct TrieNode {
    is_leaf: bool,
    nodes: HashMap<String, TrieNode>
}

impl TrieNode {
    fn new() -> Self {
        return Self {
            is_leaf: false,
            nodes: HashMap::new()
        };
    }

    fn insert(&mut self, string: &str) {
        let mut curr: &mut TrieNode = self;
        for ch in string.chars() {
            let c: String = ch.to_string();
            if !curr.nodes.contains_key(c.as_str()) {
                curr.nodes.insert(c.clone(), TrieNode::new());
            }
            curr = curr.nodes.get_mut(c.as_str()).unwrap();
        }
        curr.is_leaf = true;
    }
}

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut curr: &mut TrieNode = &mut TrieNode::new();
        let mut prefix: String = String::new();

        for word in strs.iter() {
            curr.insert(word);
        }

        for c in strs[0].chars() {
            if curr.nodes.len() > 1 || curr.is_leaf {
                break;
            }

            prefix.push(c);
            curr = curr.nodes.get_mut(c.to_string().as_str()).unwrap();
        }
        
        return prefix;
    }
}