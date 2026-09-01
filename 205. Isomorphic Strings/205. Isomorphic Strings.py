#
# Problem: 205. Isomorphic Strings
# Difficulty: Easy
# Link: https://leetcode.com/problems/isomorphic-strings/description/
# Language: python3
# Date: 2026-09-01


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a = {}
        b = {}

        for i in range(len(s)):
            if s[i] in a and a[s[i]] != t[i]:
                return False
            if t[i] in b and b[t[i]] != s[i]:
                return False
            a[s[i]] = t[i]
            b[t[i]] = s[i]

        return True
