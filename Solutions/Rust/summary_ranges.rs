/*
    [EASY]
    228. Summary Ranges

    Concepts:
    - array

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.32 MB   [Beats 21.54%]
*/
impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        if nums.is_empty() || nums.len() == 1 {
            return nums.iter().map(|&num| num.to_string()).collect::<Vec<String>>();
        }

        let mut ranges: Vec<String> = Vec::new();
        let mut rng: String = nums[0].to_string();
        let [mut last_num, mut curr_num]: [String; 2];

        for i in 1..nums.len() {
            last_num = nums[i-1].to_string();
            curr_num = nums[i].to_string();

            // if discontinuous ranges
            if nums[i] - nums[i-1] != 1 {
                if rng != last_num {
                    rng += &(String::from("->") + last_num.as_str());
                }
                ranges.push(rng.to_string());
                rng = curr_num.to_string();
            }

            // if at end of list
            if i == nums.len() - 1 {
                if rng != curr_num {
                    rng += &(String::from("->") + curr_num.as_str());
                }
                ranges.push(rng.to_string());
            }
        }

        return ranges;
    }
}