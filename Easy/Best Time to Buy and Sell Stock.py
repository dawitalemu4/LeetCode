class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left, right, profit = prices[0], prices[0], 0

        for price in prices:
            if price < left:
                left = price
                right = price
            if price > right:
                right = price
            if right - left > profit:
                profit = right - left
        
        return profit