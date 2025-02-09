/*
    [EASY]
    2621. Sleep

    Concepts:
    - promises
    - time

    Stats:
        Runtime | 54 ms     [Beats 48.93%]
        Memory  | 48.98 MB  [Beats 41.89%]
*/

/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    await new Promise((resolve) => setTimeout(resolve, millis));
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */