#
# Problem: 796. Rotate String
# Difficulty: Easy
# Link: https://leetcode.com/problems/rotate-string/
# Language: python3
# Date: 2026-09-02


# Pythonic way:
# Concatenated approach (s+s):
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        new_s = s + s

        return new_s.find(goal) != -1

'''
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        new_s = s+s

        if goal in new_s:
            return True
        else:
            return False
'''

# Brute:
'''
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
            
        n = len(s)

        for i in range(n):
            temp = s[i:] + s[:i]
            if temp == goal:
                return True
        return False
'''
