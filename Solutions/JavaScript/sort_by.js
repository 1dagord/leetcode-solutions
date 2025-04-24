/*
    [EASY]
    2724. Sort By

    Concepts:
    - JSON

    Stats:
        Runtime | 109 ms    [Beats 61.19%]
        Memory  | 69.43 MB  [Beats 90.03%]
*/

/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    return arr.sort((a, b) => {
        return (fn(a) >= fn(b)) + (fn(a) == fn(b)) - 1;
    });
};