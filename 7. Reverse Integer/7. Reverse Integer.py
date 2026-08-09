#
# Problem: 7. Reverse Integer
# Difficulty: Medium
# Link: https://leetcode.com/problems/reverse-integer/description/
# Language: python3
# Date: 2026-08-09


class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            x = 

"""# What I did (Pythonic way):
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = int(f"-{(str(x)[::-1])[:len(str(x))-1]}")
        else:
            x = int(f"{str(x)[::-1]}")

        if x > (2**31)-1 or x < -2**31:
            return 0
        else: return x
"""
