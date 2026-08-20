#
# Problem: 1886. Determine Whether Matrix Can Be Obtained By Rotation
# Difficulty: Easy
# Link: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
# Language: python3
# Date: 2026-08-20


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        els = len(mat)

        # Check 0 degrees (the original state)
        if mat == target:
            return True

        for _ in range(4):
            # 1. Transpose in-place (only iterate up to 'i' to avoid double-swapping)
            for i in range(els):
                for j in range(i):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            # 2. Reverse each row to complete the 90-degree clockwise turn
            for i in range(els):
                # Only go halfway across the row!
                for j in range(els // 2):
                    # Keep 'i' steady, and swap the left column 'j' with the right column 'els-j-1'
                    mat[i][j], mat[i][els-j-1] = mat[i][els-j-1], mat[i][j]
            
            # Pythonic way of the above loop:
            '''
            for i in range(els):
                mat[i].reverse()
            '''

            # Check the new rotated state
            if mat == target:
                return True

        return False
