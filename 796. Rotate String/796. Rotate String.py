#
# Problem: 796. Rotate String
# Difficulty: Easy
# Link: https://leetcode.com/problems/rotate-string/
# Language: python3
# Date: 2026-09-02


# Optimal:
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Guardrail: They must be the exact same length
        if len(s) != len(goal):
            return False
            
        doubled_s = s + s
        n = len(s)
        
        # Slide a window across doubled_s
        # We only need to check 'n' starting positions
        for i in range(n):
            is_match = True
            
            # Manually check character by character
            for j in range(n):
                # If any character doesn't match, this starting position is wrong
                if doubled_s[i + j] != goal[j]:
                    is_match = False
                    break
            
            # If we made it through the whole inner loop without breaking, we found it!
            if is_match:
                return True
                
        return False

# Pythonic way:
'''
# Concatenated approach (s+s):
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        new_s = s + s

        return new_s.find(goal) != -1

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
