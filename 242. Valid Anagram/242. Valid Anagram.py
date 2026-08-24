#
# Problem: 242. Valid Anagram
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-anagram/
# Language: python3
# Date: 2026-08-24


# Optimal:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must be the exact same length
        if len(s) != len(t):
            return False

        # 26 slots for lowercase English letters
        count = [0] * 26

        # Increment counts for the first string
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Decrement counts for the second string
        for ch in t:
            idx = ord(ch) - ord('a')
            count[idx] -= 1
            
            # If count drops below zero, 't' has an unmatched letter
            if count[idx] < 0:
                return False

        return True

# What i did:
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for ch in t:
            idx = ord(ch) - ord('a')
            count[idx] -= 1
            if count[idx] < 0:
                return False

        return True
'''
