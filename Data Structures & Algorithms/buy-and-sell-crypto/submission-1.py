"""
We want to return maxP.
maxP depends on the day we buy, and sell; since profit = sellP - buyP

We can init a window, where l, r = 0, shift r first, then check if prices[i] > l

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l, r = 0, 0

        while r < len(prices):
            if prices[l] < prices[r]:
                localP = prices[r] - prices[l]
                maxP = max(maxP, localP)

            else:
                l = r

            r += 1   
        
        return maxP
         
