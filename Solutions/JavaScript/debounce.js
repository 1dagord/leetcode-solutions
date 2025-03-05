/*
    [MEDIUM]
    2627. Debounce

    Concepts:
    - promises
    - time

    Stats:
        Runtime | 47 ms     [Beats 87.76%]
        Memory  | 55.14 MB  [Beats 6.32%]
*/

/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timer;
    return function(...args) {
        clearTimeout(timer);
        timer = setTimeout(() => fn(...args), t);
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */