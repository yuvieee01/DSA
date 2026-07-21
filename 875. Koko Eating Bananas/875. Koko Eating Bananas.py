#
# Problem: 875. Koko Eating Bananas
# Difficulty: Medium
# Link: https://leetcode.com/problems/koko-eating-bananas/description/
# Language: python3
# Date: 2026-07-21


import math

class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = sum(math.ceil(p / mid) for p in piles)
            print(hours)

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left
