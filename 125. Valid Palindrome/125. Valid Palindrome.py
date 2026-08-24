#
# Problem: 125. Valid Palindrome
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-palindrome/
# Language: python3
# Date: 2026-08-24


# Optimal:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            # 1. Skip non-alphanumeric from the left
            if not s[i].isalnum():
                i += 1
            # 2. Skip non-alphanumeric from the right
            elif not s[j].isalnum():
                j -= 1
            # 3. Both are valid letters/numbers, so compare them!
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
        
        return True

# Pythonic Way:
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create a cleaned list of valid, lowercase characters
        clean = [char.lower() for char in s if char.isalnum()]
        
        # Compare the list to a reversed copy of itself
        return clean == clean[::-1]
'''
