#
# Problem: 73. Set Matrix Zeroes
# Difficulty: Medium
# Link: https://leetcode.com/problems/set-matrix-zeroes/submissions/2100601109/
# Language: python3
# Date: 2026-08-09


# My approach:
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        rows_chklist = [0] * rows
        cols_chklist = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rows_chklist[i] = 1
                    cols_chklist[j] = 1
        
        for i in range(rows):
            for j in range(cols):
                if rows_chklist[i] == 1 or cols_chklist[j] == 1:
                    matrix[i][j] = 0
