#
# Problem: 121. Best Time to Buy and Sell Stock
# Difficulty: Easy
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/2100609571/
# Language: python3
# Date: 2026-08-10


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ch = float('inf')
        pro = 0

        for price in prices:
            if price < ch:
                ch = price
            elif pro < price-ch:
                pro = price-ch
        
        return pro
