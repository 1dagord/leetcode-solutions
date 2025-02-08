/*
    [EASY]
    2665. Counter II

    Concepts:
    - closures

    Stats:
        Runtime | 52 ms     [Beats 88.57%]
        Memory  | 51.93 MB  [Beats 34.22%]
*/

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let num = init;
    return {
        increment : () => ++num,
        decrement : () => --num,
        reset : () => num = init
    };
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */