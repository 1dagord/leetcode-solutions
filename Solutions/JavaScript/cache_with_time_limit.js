/*
    [MEDIUM]
    2622. Cache With Time Limit

    Concepts:
    - promises
    - time

    Stats:
        Runtime | 51 ms     [Beats 85.36%]
        Memory  | 49.78 MB  [Beats 5.62%]
*/

var TimeLimitedCache = function() {
    this.map = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    // check for membership
    let has_key = this.map.has(key);

    // clear timeout if key is present
    if (has_key)
        clearTimeout(this.map.get(key).expire);

    // store value and timeout function
    this.map.set(key, {
        value : value,
        // expired keys will automatically get deleted on expiration
        expire : setTimeout(() => this.map.delete(key), duration)
    });
    return has_key;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    return (this.map.has(key)) ? (this.map.get(key).value) : (-1);
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.map.size;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */