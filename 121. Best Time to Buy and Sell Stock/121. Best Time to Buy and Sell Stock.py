#
# Problem: 121. Best Time to Buy and Sell Stock
# Difficulty: Easy
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1959004702/
# Language: python3
# Date: 2026-03-25


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro = 0
        m = prices[0]

        for i in range(1,len(prices)):
            curr = prices[i] - m
            pro = max(curr, pro)
            m = min(prices[i], m)
        
        return pro
