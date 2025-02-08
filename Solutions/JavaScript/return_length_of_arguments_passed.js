/*
    [EASY]
    2703. Return Length of Arguments Passed

    Concepts:
    - function transformations

    Stats:
        Runtime | 54 ms     [Beats 41.99%]
        Memory  | 48.68 MB  [Beats 80.30%]
*/

/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    return args.length;
};

/**
 * argumentsLength(1, 2, 3); // 3
 */