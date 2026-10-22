class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            profit = prices[i] - least
            if prices[i] < least:
                least = prices[i]
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit

                    
