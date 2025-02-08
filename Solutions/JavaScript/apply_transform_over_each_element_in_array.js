/*
    [EASY]
    2635. Apply Transform Over Each Element in Array

    Concepts:
    - array transformations

    Stats:
        Runtime | 50 ms     [Beats 67.52%]
        Memory  | 48.91 MB  [Beats 85.79%]
*/

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    arr.forEach((num, idx) => arr[idx] = fn(num, idx));
    return arr;
};