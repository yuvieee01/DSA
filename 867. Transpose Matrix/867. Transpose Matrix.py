#
# Problem: 867. Transpose Matrix
# Difficulty: Easy
# Link: https://leetcode.com/problems/transpose-matrix/description/
# Language: python3
# Date: 2026-08-08


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        res = [[0] * rows for _ in range(cols)]     # Blank 2D matrix canvas..

        for i in range(rows):
            for j in range(cols):
                res[j][i] = matrix[i][j]
        
        return res

'''
don't create Blank 2D matrix canvas like:
    res = [[0] * rows] * cols
because, in python, It looks completely logical, but it creates a massive bug. When you use the * operator to multiply a list containing another list, Python does not create independent copies of the inner list. Instead, it creates multiple references to the exact same list in memory.
'''
