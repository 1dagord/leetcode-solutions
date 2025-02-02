/*
    [EASY]
    169. Majority Element

    Concepts:
    - array
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 51.29 MB  [Beats 90.78%]
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    // Moore's Voting Algorithm
    let count = 0, candidate = 0;

    for (let i = 0; i < nums.length; i++) {
        if (!count) { candidate = nums[i]; }
        if (nums[i] == candidate) { count++; }
        else { count--; }
    }
    return candidate;
};