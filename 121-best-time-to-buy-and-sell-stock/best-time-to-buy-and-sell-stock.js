/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let buy_price = prices[0];
    let profit = 0;

    for(let i = 1; i < prices.length; i++){
        if(buy_price > prices[i]){
            buy_price = prices[i];
        }
        profit = Math.max(profit,prices[i]-buy_price);
    }
    return profit;
};