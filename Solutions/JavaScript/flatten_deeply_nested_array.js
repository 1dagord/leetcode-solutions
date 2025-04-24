/*
    [MEDIUM]
    2625. Flatten Deeply Nested Array

    Concepts:
    - JSON

    Stats:
        Runtime | 152 ms    [Beats 33.61%]
        Memory  | 93.53 MB  [Beats 13.81%]
*/

/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    function recurse(obj, depth) {
        if (depth === 0)
            return obj;

        let res = [];

        obj.forEach((val) => {
            if (!Array.isArray(val))
                res.push(val);
            else
                res.push(...recurse(val, depth - 1));
        });
        
        return res;
    }
    return recurse(arr, n);
};