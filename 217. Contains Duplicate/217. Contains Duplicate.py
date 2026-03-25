#
# Problem: 217. Contains Duplicate
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate/submissions/1959148530/
# Language: python3
# Date: 2026-03-25


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False
