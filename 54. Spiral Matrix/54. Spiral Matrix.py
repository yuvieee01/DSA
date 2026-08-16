#
# Problem: 54. Spiral Matrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/spiral-matrix/description/
# Language: python3
# Date: 2026-08-16


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])

        row_strt, row_end = 0, row-1
        col_strt, col_end = 0, col-1

        ans = []

        while len(ans) < row*col:
            # row_strt : col_strt -> col_end
            for i in range(col_strt, col_end+1):
                ans.append(matrix[row_strt][i])
            row_strt += 1

            if len(ans) == row*col:
                break
            
            # col_end : row_strt -> row_end
            for i in range(row_strt, row_end+1):
                ans.append(matrix[i][col_end])
            col_end -= 1

            if len(ans) == row*col:
                break
            
            # row_end : col_end -> col_strt
            for i in range(col_end, col_strt-1, -1):
                ans.append(matrix[row_end][i])
            row_end -= 1

            if len(ans) == row*col:
                break
            
            # col_strt : row_end -> row_strt
            for i in range(row_end, row_strt-1, -1):
                ans.append(matrix[i][col_strt])
            col_strt += 1
        
        return ans
