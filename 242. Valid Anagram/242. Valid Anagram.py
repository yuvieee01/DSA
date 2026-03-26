#
# Problem: 242. Valid Anagram
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-anagram/description/
# Language: python3
# Date: 2026-03-26


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in t:
            if i not in d:
                return False
            else:
                if d[i] == 0:
                    return False
                d[i]-=1
        return True
