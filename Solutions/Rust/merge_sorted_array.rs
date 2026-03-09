/*
    [EASY]
    88. Merge Sorted Array

    Concepts:
    - two pointers
    - sorting

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 2.33 MB   [Beats 1.09%]
*/

impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        let (mut i, mut j) = (0 as usize, 0 as usize);
        while (
            i < (m + n).try_into().unwrap()
            && j < n.try_into().unwrap()
        ) {
            if nums1[i] > nums2[j] {
                nums1.splice(i..i, [nums2[j]].iter().cloned());
                j += 1;
            } else { i += 1; }
        }

        while j < n.try_into().unwrap() {
            nums1[m as usize + j] = nums2[j];
            j += 1;
        }

        nums1.drain((m + n) as usize..nums1.len());
    }
}