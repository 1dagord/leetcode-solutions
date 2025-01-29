/*
    [EASY]
    1. Two Sum

    Concepts:
    - array
    - hash table

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 52.16 MB  [Beats 10.59%]
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map();

    nums.forEach((num, idx) => map.set(num, idx));

    for (let i = 0; i < nums.length; i++) {
        if (map.has(target - nums[i]) && i != map.get(target - nums[i])) {
            return [i, map.get(target - nums[i])];
        }
    }

};