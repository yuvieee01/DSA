#
# Problem: 73. Set Matrix Zeroes
# Difficulty: Medium
# Link: https://leetcode.com/problems/set-matrix-zeroes/
# Language: python3
# Date: 2026-08-20


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """Do not return anything, modify matrix in-place instead."""
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False

        # 1. Check if the first row has any zeroes
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_zero = True
                break

        # 2. Use the first row & first column as markers for the rest (rows 1..rows-1)
        for r in range(1, rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        # 3. Update the inner matrix using the markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # 4. Zero out the first column if the first cell marker was triggered
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # 5. Zero out the first row if flagged originally
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0

# What I tried (Wrong) only 149 / 211 testcases passed:
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

Two specific logic issues remain:

Scouting the First Row: In your second loop (where you set markers on the borders), starting at row = 0 can overwrite matrix[0][0] if matrix[0][col] == 0. Start that loop at row = 1 so row 0 markers are handled purely by first_row_zero.

Final Border Handling: You do not need a nested loop under if first_row_zero:. You only need to zero out the first column (if matrix[0][0] == 0) and the first row (if first_row_zero is true).
'''

# My approach [O(m + n) - space]:
'''
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
