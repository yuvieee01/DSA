#
# Problem: 1957. Delete Characters to Make Fancy String
# Difficulty: Easy
# Link: https://leetcode.com/problems/delete-characters-to-make-fancy-string/submissions/2127316773/
# Language: python3
# Date: 2026-09-01


class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for char in s:
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                continue
            res.append(char)
        return "".join(res)
