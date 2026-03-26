#
# Problem: 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Language: python3
# Date: 2026-03-26


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        set1 = set({})

        i, j = 0, 1
        set1.add(s[i])
        ans = 1

        while j < n:
            while s[j] in set1:
                set1.discard(s[i])
                i+=1

            set1.add(s[j])
            j += 1
            ans = max(ans, j-i)
        
        return ans
