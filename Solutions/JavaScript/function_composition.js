/*
    [EASY]
    2629. Function Composition

    Concepts:
    - function transformations

    Stats:
        Runtime | 64 ms     [Beats 57.57%]
        Memory  | 50.07 MB  [Beats 68.88%]
*/

/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        return functions.reduceRight((y, fn) => fn(y), x);
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */