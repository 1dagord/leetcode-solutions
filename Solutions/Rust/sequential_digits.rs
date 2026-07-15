/*
    [MEDIUM]
    1291. Sequential Digits

    Concepts:
    - backtracking
    - enumeration

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.20 MB   [Beats 50.48%]
*/
impl Solution {
    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32> {
        let nums = (1..=9)
            .map(|v| (v + '0' as u8) as char)
            .collect::<Vec<char>>();
        let mut sequence: Vec<i32> = Vec::new();

        fn build_sequence(
            low: i32,
            high: i32,
            sequence: &mut Vec<i32>,
            seq: String,
            remaining: Vec<char>,
        ) -> bool {
            if let Ok(num) = seq.parse::<i32>() {
                if low <= num && num <= high {
                    sequence.push(num);
                } else if num > high {
                    return false;
                }

                for c in remaining.iter() {
                    if !build_sequence(
                        low,
                        high,
                        sequence,
                        [seq.clone(), c.to_string()].join(""),
                        remaining[1..].to_vec(),
                    ) {
                        return false;
                    }
                }

                return false;
            } else {
                return false;
            }
        }

        for (i, num) in nums.iter().enumerate() {
            build_sequence(
                low,
                high,
                &mut sequence,
                num.to_string(),
                nums[i + 1..].to_vec(),
            );
        }

        sequence.sort();
        return sequence;
    }
}
