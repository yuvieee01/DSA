#
# Problem: 73. Set Matrix Zeroes
# Difficulty: Medium
# Link: https://leetcode.com/problems/set-matrix-zeroes/
# Language: python3
# Date: 2026-08-18


'''
# What I tried (Wrong) only 149 / 211 testcases passed:
Two specific logic issues remain:

Scouting the First Row: In your second loop (where you set markers on the borders), starting at row = 0 can overwrite matrix[0][0] if matrix[0][col] == 0. Start that loop at row = 1 so row 0 markers are handled purely by first_row_zero.

Final Border Handling: You do not need a nested loop under if first_row_zero:. You only need to zero out the first column (if matrix[0][0] == 0) and the first row (if first_row_zero is true).
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """Do not return anything, modify matrix in-place instead."""

        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False

        for col in range(cols):
            if matrix[0][col] == 0:
                first_row_zero = True

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if first_row_zero:
            for row in range(rows):
                for col in range(cols):
                    if matrix[0][col] == 0:
                        matrix[row][col] = 0
            for col in range(cols):
                matrix[0][col] = 0

'''
# My approach [O(m + n) - space]:
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
'''
