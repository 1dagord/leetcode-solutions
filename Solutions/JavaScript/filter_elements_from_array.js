/*
    [EASY]
    2634. Filter Elements from Array

    Concepts:
    - array transformations

    Stats:
        Runtime | 50 ms     [Beats 75.01%]
        Memory  | 49.15 MB  [Beats 39.62%]
*/

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let res = [];
    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) res.push(arr[i]);
    }
    return res;
};

// imitates built-in `Array.filter` function