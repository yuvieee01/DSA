#
# Problem: 242. Valid Anagram
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-anagram/
# Language: python3
# Date: 2026-08-24


# Optimal:
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map frequency tuples to lists of anagrams
        anagram_map = defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            
            # Build the 26-slot signature for the current word
            for char in word:
                count[ord(char) - ord('a')] += 1
                
            # Tuples are immutable, making them valid dictionary keys
            anagram_map[tuple(count)].append(word)
            
        # Return all the grouped lists
        return list(anagram_map.values())

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
