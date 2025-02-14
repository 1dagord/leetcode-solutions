/*
    [EASY]
    2626. Array Reduce Transformation

    Concepts:
    - array transformations

    Stats:
        Runtime | 57 ms     [Beats 40.61%]
        Memory  | 49.74 MB  [Beats 20.53%]
*/

/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let res = init;
    for (const num of nums) {
        res = fn(res, num);
    }
    return res;
};

// imitates built-in `Array.reduce` function