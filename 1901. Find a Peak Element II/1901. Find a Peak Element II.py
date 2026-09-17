#
# Problem: 1901. Find a Peak Element II
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-a-peak-element-ii/
# Language: python3
# Date: 2026-09-17


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])

        left = 0
        right = cols - 1
        
        while left < right:
            mid_col = left + (right - left) // 2

            max_row = 0 # Find the row index of the maximum element in the current mid_col
            for row in range(1, rows):
                if mat[row][mid_col] > mat[max_row][mid_col]:
                    max_row = row

            curr_val = mat[max_row][mid_col]

            # Get the values of left and right neighbors (use -1 if out of bounds)
            left_val = mat[max_row][mid_col - 1] if mid_col-1 >= 0 else -1
            right_val = mat[max_row][mid_col + 1] if mid_col+1 < cols else -1

            # We only check to the left & right of the curr val as curr val is already > up & down
            if left_val < curr_val > right_val:
                return [max_row, mid_col]
            
            elif curr_val < right_val:
                left = mid_col + 1

            else:
                right = mid_col - 1

        return []
