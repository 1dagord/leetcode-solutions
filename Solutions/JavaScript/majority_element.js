/*
    [EASY]
    169. Majority Element

    Concepts:
    - array
    - hash table

    Stats:
        Runtime | 5 ms      [Beats 52.38%]
        Memory  | 51.30 MB  [Beats 90.78%]
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let half_length = ~~(nums.length / 2);
    let counter = new Map();

    for (const num of nums) {
        if (counter.has(num)) {
            counter.set(num, counter.get(num) + 1);
        } else {
            counter.set(num, 1);
        }

        if (counter.get(num) > half_length) {
            return num;
        }
    }
};