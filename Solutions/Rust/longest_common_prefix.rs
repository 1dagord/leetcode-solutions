/*
    [EASY]
    14. Longest Common Prefix

    Concepts:
    - string
    - trie

    Stats:
        Runtime | 1 ms      [Beats 15.80%]
        Memory  | 2.28 MB   [Beats 61.66%]
*/
use std::collections::HashMap;

struct TrieNode {
    is_leaf: bool,
    nodes: HashMap<char, TrieNode>
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
        for c in string.chars() {
            if !curr.nodes.contains_key(&c) {
                curr.nodes.insert(c, TrieNode::new());
            }
            curr = curr.nodes.get_mut(&c).unwrap();
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
            curr = curr.nodes.get_mut(&c).unwrap();
        }
        
        return prefix;
    }
}