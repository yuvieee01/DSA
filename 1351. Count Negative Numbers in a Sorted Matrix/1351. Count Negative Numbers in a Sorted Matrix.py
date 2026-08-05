#
# Problem: 1351. Count Negative Numbers in a Sorted Matrix
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# Language: python3
# Date: 2026-08-05


# Brute Force:
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = 0
        for col in grid:
            for row in col:
                if row < 0:
                    neg += 1
        
        return neg
