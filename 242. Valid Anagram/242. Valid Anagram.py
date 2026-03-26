#
# Problem: 242. Valid Anagram
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-anagram/
# Language: python3
# Date: 2026-03-26


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
