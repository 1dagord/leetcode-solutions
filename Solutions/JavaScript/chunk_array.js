/*
    [EASY]
    2677. Chunk Array

    Concepts:
    - JSON

    Stats:
        Runtime | 50 ms     [Beats 84.15%]
        Memory  | 52.26 MB  [Beats 11.70%]
*/

/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const res = [];
    for (let i = 0; i < arr.length; i += size) {
        res.push(arr.slice(i, i + size));
    }
    return res;
};

// imitates Lodash's `_.chunk` function
