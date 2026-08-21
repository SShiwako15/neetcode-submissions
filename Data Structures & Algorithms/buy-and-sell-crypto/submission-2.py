class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        profit = 0
        for i in range(len(prices)):
            if buy > prices[i]:
                buy = prices[i]
                sell = 0
            elif buy < prices[i]:
                sell = prices[i]
            profit = max(profit, sell - buy)
        return profit
            

            