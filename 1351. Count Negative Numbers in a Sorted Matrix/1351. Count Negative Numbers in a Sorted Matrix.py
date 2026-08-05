#
# Problem: 1351. Count Negative Numbers in a Sorted Matrix
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# Language: python3
# Date: 2026-08-05


# Optimal Approach (Staircase Walk):
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # Start at the top-right corner
        r = 0
        c = cols - 1
        
        neg_count = 0
        
        # Walk the staircase until we fall off the bottom or the left edge
        while r < rows and c >= 0:
            if grid[r][c] < 0:
                # If it's negative, everything below it in this column is also negative.
                # (Total rows - current row index) gives us the remaining vertical block.
                neg_count += (rows - r)
                
                # Move left to evaluate the next column
                c -= 1
            else:
                # If it's >= 0, we need a smaller number, so we move down
                r += 1
                
        return neg_count

'''
# Brute Force:
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = 0
        for col in grid:
            for row in col:
                if row < 0:
                    neg += 1
        
        return neg
'''
