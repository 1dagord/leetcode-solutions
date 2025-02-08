/*
    [EASY]
    2723. Add Two Promises

    Concepts:
    - promises
    - time

    Stats:
        Runtime | 65 ms     [Beats 45.12%]
        Memory  | 49.54 MB  [Beats 64.26%]
*/

/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    const [v1, v2] = await Promise.all([promise1, promise2]);
    return v1 + v2;
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */