#
# Problem: 49. Group Anagrams
# Difficulty: Medium
# Link: https://leetcode.com/problems/group-anagrams/description/
# Language: python3
# Date: 2026-03-26


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())
