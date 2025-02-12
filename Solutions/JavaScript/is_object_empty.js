/*
    [EASY]
    2727. Is Object Empty

    Concepts:
    - JSON

    Stats:
        Runtime | 40 ms     [Beats 97.74%]
        Memory  | 50.52 MB  [Beats 14.70%]
*/

/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    return ["{}", "[]"].includes(JSON.stringify(obj));
};