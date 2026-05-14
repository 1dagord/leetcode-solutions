/*
    [EASY]
    383. Ransom Note

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 2 ms      [Beats 44.14%]
        Memory  | 2.24 MB   [Beats 55.17%]
*/
use std::collections::HashMap;

impl Solution {
    pub fn can_construct(ransom_note: String, magazine: String) -> bool {
        let [mut note, mut mag] = [HashMap::new(), HashMap::new()];
        for (s, mut map) in [(ransom_note, &mut note), (magazine, &mut mag)] {
            s
                .chars()
                .for_each(|c| {
                    map
                        .entry(c)
                        .and_modify(|v| *v += 1)
                        .or_insert(1);
                });
        }

        for (key, val) in note {
            match mag.get(&key) {
                Some(&v) => {
                    if val > v { return false; }
                },
                None => { return false; }
            }
        }

        return true;
    }
}