class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0:
            return 0
        else:
            max_profit = 0
            min_price = prices[0]
            for a in range(len(prices)):
                profit = prices[a] - min_price
                max_profit = max(profit, max_profit)
                min_price = min(min_price, prices[a])

            return max_profit