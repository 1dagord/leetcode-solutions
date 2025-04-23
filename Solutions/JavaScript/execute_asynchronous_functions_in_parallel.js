/*
    [MEDIUM]
    2721. Execute Asynchronous Functions in Parallel

    Concepts:
    - promises
    - time

    Stats:
        Runtime | 60 ms     [Beats 58.19%]
        Memory  | 54.23 MB  [Beats 66.82%]
*/

/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    let results = [];
    let resolved = 0;

    return new Promise((resolve, reject) => {
        functions.forEach((f, idx) => 
            f()
            .then(result => {
                results[idx] = result;
                resolved += 1;
                if (resolved == functions.length)
                    resolve(results);
            })
            .catch(error => reject(error))
        )
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */