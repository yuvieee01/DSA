#
# Problem: 14. Longest Common Prefix
# Difficulty: Easy
# Link: https://leetcode.com/problems/longest-common-prefix/
# Language: python3
# Date: 2026-08-10


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

