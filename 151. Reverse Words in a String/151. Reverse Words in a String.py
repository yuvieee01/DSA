#
# Problem: 151. Reverse Words in a String
# Difficulty: Medium
# Link: https://leetcode.com/problems/reverse-words-in-a-string/
# Language: python3
# Date: 2026-09-01


# Pythonic Way:
class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        s = s.strip()
        s = s.split()
        s.reverse()
        s = " ".join(s)
        return s
        '''

        # OR one liner:
        return " ".join((s.strip().split())[::-1])
