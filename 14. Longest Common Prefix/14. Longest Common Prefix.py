#
# Problem: 14. Longest Common Prefix
# Difficulty: Easy
# Link: https://leetcode.com/problems/longest-common-prefix/description/
# Language: python3
# Date: 2026-09-04


# The pythonic way:
# and probably the fastest way on lc
# because the .sort() is written in C
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        # Sort the array alphabetically
        strs.sort()
        
        # We only care about the first and last words now
        first = strs[0]
        last = strs[-1]
        
        res = ""
        
        # Compare letters one by one, up to the length of the shorter word
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return res
            res += first[i]
            
        return res

'''
# My approach:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: if the list is empty, there is no prefix
        if not strs:
            return ""
            
        res = ""
        c = 0
        
        # Loop based on the length of the FIRST word
        while c < len(strs[0]):
            temp = strs[0][c]
            
            for i in strs:
                # Bail out if we hit the end of a short word OR the letters don't match
                if c == len(i) or i[c] != temp:
                    return res
                    
            res = res + temp
            c += 1

        return res

'''
