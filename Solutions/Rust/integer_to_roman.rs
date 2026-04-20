/*
    [MEDIUM]
    12. Integer to Roman

    Concepts:
    - string
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.20 MB   [Beats 57.49%]
*/
use std::collections::BTreeMap;

impl Solution {
    pub fn int_to_roman(mut num: i32) -> String {
        let mut roman_nums: BTreeMap<i32, &str> = BTreeMap::from([
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]);

        let mut roman = String::from("");
        let mut roman_count: BTreeMap<i32, i32> = BTreeMap::new();

        for (k, v) in roman_nums.iter().rev() {
            while num >= *k {
                roman_count.entry(*k).and_modify(|x| *x += 1).or_insert(1);
                num -= *k;
            }
        }

        for (k, v) in roman_count.iter().rev() {
            for i in 0..*v {
                roman.push_str(roman_nums.get(k).unwrap());
            }
        }

        return roman;
    }
}