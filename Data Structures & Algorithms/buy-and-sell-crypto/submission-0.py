class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leny = len(prices)
        largest = 0
        for i in range(leny) :
            for j in range(i+1, leny):
                largest = max(largest,(prices[j]- prices[i]))

        return largest