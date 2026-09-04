#
# Problem: 1614. Maximum Nesting Depth of the Parentheses
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# Language: python3
# Date: 2026-09-04


class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        current_depth = 0
        for char in s:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
        return max_depth
