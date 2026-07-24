#
# Problem: 268. Missing Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/missing-number/
# Language: python3
# Date: 2026-07-24


from collections import defaultdict
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mp = defaultdict(int)

        for num in nums:
            if not mp.get(num, 0):
                mp[num] += 1

        for i in range(len(nums)+1):
            if not mp.get(i,0):
                return i
        
        return -1
