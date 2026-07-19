class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Profit =0

        for i in range(len(prices)-1):

            for j in range(i+1,len(prices)):
                if (prices[j]-prices[i])>Profit:
                    Profit =prices[j] - prices[i]
        
        if Profit>0:
            return Profit
        else:
            return 0


