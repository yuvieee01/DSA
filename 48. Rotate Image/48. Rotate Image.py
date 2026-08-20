#
# Problem: 48. Rotate Image
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotate-image/
# Language: python3
# Date: 2026-08-20


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Do not return anything, modify matrix in-place instead."""
        els = len(matrix)

        # 1. Transpose in-place (only iterate up to 'i' to avoid double-swapping)
        for i in range(els):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 2. Reverse each row to complete the 90-degree clockwise turn
        for i in range(els):
            # Only go halfway across the row!
            for j in range(els // 2):
                # Keep 'i' steady, and swap the left column 'j' with the right column 'els-j-1'
                matrix[i][j], matrix[i][els-j-1] = matrix[i][els-j-1], matrix[i][j]
            
        # 2. Pythonic way of the above loop:
        '''
        for i in range(els):
            mat[i].reverse()
        '''
