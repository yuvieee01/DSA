#
# Problem: 121. Best Time to Buy and Sell Stock
# Difficulty: Easy
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/2086560997/
# Language: python3
# Date: 2026-07-29


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro = 0
        ch = prices[0]

        for i in range(len(prices)):
            ch = min(ch, prices[i])
            pro = max(pro, prices[i]-ch)
        
        return pro
