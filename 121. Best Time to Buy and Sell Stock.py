from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSalePrice = 0
        maxProfit = 0

        for i in range(len(prices)-1, -1, -1):
            if prices[i] > maxSalePrice:
                maxSalePrice = prices[i]
            else:
                currentProfit = maxSalePrice - prices[i]
                maxProfit = max(maxProfit, currentProfit)
        return maxProfit


solution = Solution()
list = [7,1,5,3,6,4]
print(solution.maxProfit([7,1,5,3,6,4])) #5
print(solution.maxProfit([7,6,4,3,1]))  #0
