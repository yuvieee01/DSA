#
# Problem: 2643. Row With Maximum Ones
# Difficulty: Easy
# Link: https://leetcode.com/problems/row-with-maximum-ones/
# Language: python3
# Date: 2026-09-13


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_row = 0
        max_ones = 0

        for i in range(len(mat)):
            ones = sum (mat[i])

            if ones > max_ones:
                max_ones = ones
                max_row = i
            
        return [max_row, max_ones]
