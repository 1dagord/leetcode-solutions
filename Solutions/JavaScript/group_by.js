/*
    [MEDIUM]
    2631. Group By

    Concepts:
    - JSON

    Stats:
        Runtime | 94 ms     [Beats 83.52%]
        Memory  | 77.46 MB  [Beats 64.57%]
*/

/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    let grouped = new Map();

    this.forEach((obj) => {
        const output = fn(obj);

        if (grouped.has(output))
            grouped.get(output).push(obj);
        else
            grouped.set(output, [obj]);
    });
    
    return Object.fromEntries(grouped);
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */

// imitates Lodash's `_.groupBy` function