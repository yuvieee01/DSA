#
# Problem: 240. Search a 2D Matrix II
# Difficulty: Medium
# Link: https://leetcode.com/problems/search-a-2d-matrix-ii/description/
# Language: python3
# Date: 2026-09-15


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        row, col = 0, cols - 1

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False
