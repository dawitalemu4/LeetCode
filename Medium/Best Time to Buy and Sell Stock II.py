class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        temp = prices[len(prices)-1] - prices[0]
        profit = 0 

        for i in range(len(prices)):
            if i + 1 < len(prices) and prices[i+1] - prices[i] > 0:
                profit += prices[i+1] - prices[i]
            if i + 1 < len(prices) and prices[i+1] - prices[i] > profit:
                profit -= prices[i] 
                profit += prices[i+1] - prices[i]
        
        return max(profit, temp)