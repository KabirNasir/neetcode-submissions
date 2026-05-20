class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leny = len(prices)
        l,r=0,1
        largest = 0
        while(r<leny):
            if(prices[r] < prices[l]):
                l=r
                
            else:
                largest = max(largest,(prices[r]-prices[l]))
            r+=1
        return largest