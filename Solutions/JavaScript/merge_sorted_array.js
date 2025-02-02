/*
    [EASY]
    88. Merge Sorted Array

    Concepts:
    - array
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 48.87 MB  [Beats 82.04%]
*/

/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    const nums3 = new Array(m+n);
    let i = 0, j = 0;

    while (i < m && j < n) {
        nums3[i+j] = (nums1[i] < nums2[j]) ? (nums1[i++]) : (nums2[j++]);
    }
    while (i < m) {
        nums3[n+i] = nums1[i++];
    }
    while (j < n) {
        nums3[m+j] = nums2[j++];
    }
    
    nums3.forEach((num, idx) => nums1[idx] = num);
};