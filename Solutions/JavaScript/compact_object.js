/*
    [MEDIUM]
    2705. Compact Object

    Concepts:
    - JSON

    Stats:
        Runtime | 69 ms     [Beats 64.71%]
        Memory  | 67.85 MB  [Beats 38.48%]
*/

/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (typeof obj !== "object" || obj === null)
        return obj;

    if (Array.isArray(obj))
        return obj.filter(Boolean).map(compactObject);

    const res = {};
    for (const key in obj) {
        if (obj[key])
            res[key] = (typeof obj[key] === "object") ? compactObject(obj[key]) : obj[key];
    }

    return res;
};