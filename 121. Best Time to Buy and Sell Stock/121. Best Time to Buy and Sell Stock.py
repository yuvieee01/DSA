#
# Problem: 121. Best Time to Buy and Sell Stock
# Difficulty: Easy
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/2086568604/
# Language: python3
# Date: 2026-07-29


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro = 0
        ch = prices[0]

        for price in prices:
            if price < ch:
                ch = price
            if pro < price-ch:
                pro = price-ch
        
        return pro
