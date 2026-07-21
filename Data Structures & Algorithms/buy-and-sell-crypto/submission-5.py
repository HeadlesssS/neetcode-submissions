class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Profit =0
        min =prices[0]
        if len(prices) == 0 or len(prices) ==1: return 0

        for i in range(len(prices)):
            if prices[i]<min:
                min = prices[i]
            if (prices[i] - min)>Profit:
                Profit = (prices[i] - min)
        
        
        return Profit
