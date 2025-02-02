/*
    [EASY]
    121. Best Time to Buy and Sell Stock

    Concepts:
    - array

    Stats:
        Runtime | 3 ms      [Beats 53.91%]
        Memory  | 59.47 MB  [Beats 33.63%]
*/

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let profit = 0;
    let min_price = Number.MAX_SAFE_INTEGER;

    for (const price of prices) {
        if (price < min_price) { min_price = price; }
        if (price - min_price > profit) { profit = price - min_price; }
    }
    return profit;
};