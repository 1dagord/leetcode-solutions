/*
    [MEDIUM]
    2623. Memoize

    Concepts:
    - function transformations

    Stats:
        Runtime | 285 ms    [Beats 69.67%]
        Memory  | 91.64 MB  [Beats 7.61%]
*/

/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    // cache stores arrays by reference
    // convert to string to force cache hit
    const cache = new Map();
    return function(...args) {
        const key = JSON.stringify(args);
        if (cache.has(key)) {
            return cache.get(key);
        }
        const res = fn(...args);
        cache.set(key, res);
        return res;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */