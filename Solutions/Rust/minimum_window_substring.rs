/*
    [HARD]
    76. Minimum Window Substring

    Concepts:
    - sliding window
    - hash table

    Stats:
        Runtime | 4 ms      [Beats 52.63%]
        Memory  | 2.46 MB   [Beats 38.60%]
*/
use std::collections::HashMap;

impl Solution {
    pub fn min_window(s: String, t: String) -> String {
        let [m, n] = [s.len(), t.len()];
        if m < n { return String::from(""); }
        let [s_chars, t_chars] = [
            s.chars().collect::<Vec<char>>(),
            t.chars().collect::<Vec<char>>()
        ];

        let mut t_count: HashMap<char, i32> = HashMap::new();
        t_chars
            .iter()
            .for_each(|&c| {
                t_count
                    .entry(c)
                    .and_modify(|v| *v += 1)
                    .or_insert(1);
            });

        let mut window = [0, i32::MAX];
        let [mut start, mut finish]: [i32; 2] = [0, n as i32];

        for (end, c) in s.chars().enumerate() {
            match t_count.get(&c) {
                Some(&v) => {
                    if v > 0 { finish -= 1; }
                },
                None => { t_count.insert(c, 0); }
            }

            t_count.entry(c).and_modify(|v| *v -= 1);

            if finish == 0 {
                while *t_count.entry(s_chars[start as usize]).or_insert(0) != 0 {
                    t_count.entry(s_chars[start as usize]).and_modify(|v| *v += 1);
                    start += 1;
                }
                if end as i32 - start < window[1] - window[0] {
                    window = [start, end as i32];
                }

                t_count.entry(s_chars[start as usize]).and_modify(|v| *v += 1);
                [start, finish] = [start + 1, finish + 1];
            }
        }

        return if window[1] > m as i32 {
            String::from("")
        } else {
            String::from(&s[window[0] as usize..=window[1] as usize])
        }
    }
}