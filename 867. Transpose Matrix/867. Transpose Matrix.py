#
# Problem: 867. Transpose Matrix
# Difficulty: Easy
# Link: https://leetcode.com/problems/transpose-matrix/
# Language: python3
# Date: 2026-08-06


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        res = [[0] * rows for _ in range(cols)]     # Blank 2D matrix canvas..

        for i in range(rows):
            for j in range(cols):
                res[j][i] = matrix[i][j]
        
        return res
