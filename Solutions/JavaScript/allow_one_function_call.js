/*
    [EASY]
    2666. Allow One Function Call

    Concepts:
    - function transformations

    Stats:
        Runtime | 40 ms     [Beats 97.92%]
        Memory  | 49.23 MB  [Beats 11.11%]
*/

/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let is_called = false;
    return function(...args){
        if (!is_called) {
            is_called = true;
            return fn(...args);
        }
        return undefined;
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */