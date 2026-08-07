#
# Problem: 1572. Matrix Diagonal Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/matrix-diagonal-sum/submissions/2098325342/
# Language: python3
# Date: 2026-08-07


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = 0
        for i in range(n):
            s += mat[i][i]
            
            if i != n - 1 - i:
                s += mat[i][n - 1 - i]
        
        return s
