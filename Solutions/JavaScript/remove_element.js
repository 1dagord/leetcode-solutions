/*
    [EASY]
    27. Remove Element

    Concepts:
    - array
    - two pointers

    Stats:
        Runtime | 0 ms      [Beats 100%]
        Memory  | 50.00 MB  [Beats 7.79%]
*/

/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    for (let i = 0; i < nums.length;) {
        if (nums[i] == val) {
            nums.splice(i, 1);
        } else {
            i++;
        }
    }

    return nums.length;
};