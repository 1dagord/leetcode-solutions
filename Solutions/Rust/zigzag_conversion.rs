/*
    [MEDIUM]
    6. Zigzag Conversion

    Concepts:
    - string

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.32 MB   [Beats 39.26%]
*/
impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        let mut str_dirs: Vec<(char, i32)> = Vec::new();
        let mut is_moving_down: bool = true;
        let mut k: i32 = 0;

        for (i, c) in s.chars().enumerate() {
            str_dirs.push((c, k));
            k += if is_moving_down { 1 } else { -1 };

            if k == 0 {
                is_moving_down = true;
            } else if k == num_rows - 1 {
                is_moving_down = false;
            }
        }

        str_dirs.sort_by_key(|&item| item.1);
        return str_dirs
            .into_iter()
            .map(|item| item.0)
            .collect();
    }
}