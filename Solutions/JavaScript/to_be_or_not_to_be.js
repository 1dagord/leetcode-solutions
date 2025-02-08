/*
    [EASY]
    2704. To Be Or Not To Be

    Concepts:
    - closures

    Stats:
        Runtime | 45 ms     [Beats 90.40%]
        Memory  | 48.98 MB  [Beats 43.92%]
*/

/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe : (val2) => {
            if (val === val2) { return true; }
            throw "Not Equal";
        },
        notToBe : (val3) => {
            if (val !== val3) { return true; }
            throw "Equal";
        }
    };
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */