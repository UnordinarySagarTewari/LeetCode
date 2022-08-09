class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy=10**4+1
        maxProf=0
        for i in range(len(prices)):
            minBuy=min(minBuy,prices[i])
            maxProf=max(maxProf,prices[i]-minBuy)
        return maxProf
                
