/*
    [EASY]
    2667. Create Hello World Function

    Concepts:
    - closures

    Stats:
        Runtime | 44 ms     [Beats 87.96%]
        Memory  | 49.02 MB  [Beats 16.23%]
*/

/**
 * @return {Function}
 */
var createHelloWorld = function() {
    return (...args) => "Hello World";
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */