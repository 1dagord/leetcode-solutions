/*
    [EASY]
    2619. Array Prototype Last

    Concepts:
    - JSON

    Stats:
        Runtime | 34 ms     [Beats 88.24%]
        Memory  | 54.67 MB  [Beats 6.12%]
*/

/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    return (this.length == 0) ? -1 : this[this.length - 1];
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */