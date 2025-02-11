/*
    [EASY]
    2695. Array Wrapper

    Concepts:
    - classes

    Stats:
        Runtime | 53 ms     [Beats 60.34%]
        Memory  | 49.82 MB  [Beats 90.67%]
*/

/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
    this.arr = nums;
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    return (this.arr) ? (this.arr.reduce((a, b) => a + b, 0)) : 0;
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    return JSON.stringify(this.arr);
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */