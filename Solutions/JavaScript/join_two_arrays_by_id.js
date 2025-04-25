/*
    [MEDIUM]
    2722. Join Two Arrays by ID

    Concepts:
    - JSON

    Stats:
        Runtime | 303 ms    [Beats 47.19%]
        Memory  | 100.49 MB [Beats 65.98%]
*/

/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const joined = new Map();

    arr1.forEach((obj) => {
        joined.set(obj.id, obj);
    });
    
    arr2.forEach((obj) => {
        if (joined.has(obj.id))
            joined.set(obj.id, { ...joined.get(obj.id), ...obj });
        else
            joined.set(obj.id, obj);
    });

    let joinedArray = Array.from(joined.values());
    joinedArray.sort((a, b) => a.id - b.id);
    return joinedArray;
};