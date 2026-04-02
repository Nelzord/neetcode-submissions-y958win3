class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mostProfit = 0
        lowestSeen = prices[0] 
        for i in range(1, len(prices)):
            if prices[i] - lowestSeen > mostProfit:
                mostProfit = prices[i] - lowestSeen
            lowestSeen = min(lowestSeen, prices[i])
            
        return mostProfit