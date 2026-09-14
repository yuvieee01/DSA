#
# Problem: 74. Search a 2D Matrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/search-a-2d-matrix/
# Language: python3
# Date: 2026-09-14


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            mid = left + (right - left) // 2

            row = mid // n
            col = mid % n

            value = matrix[row][col]

            if value == target:
                return True

            if value < target:
                left = mid + 1
            
            else:
                right = mid - 1

        return False
