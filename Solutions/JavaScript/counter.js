/*
    [EASY]
    2620. Counter

    Concepts:
    - closures

    Stats:
        Runtime | 33 ms     [Beats 99.78%]
        Memory  | 48.20 MB  [Beats 94.91%]
*/

/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    return () => n++;
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */