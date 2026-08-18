class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        buy = prices[0]
        sell = prices[0]
        profit = 0
        for num in prices:
            if num > sell:
                sell = num
            if (sell - buy) > profit:
                profit = sell - buy
            if num < buy:
                buy = num
                sell = num
                
        return profit
            