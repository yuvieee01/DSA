#
# Problem: 485. Max Consecutive Ones
# Difficulty: Easy
# Link: https://leetcode.com/problems/max-consecutive-ones/description/
# Language: python3
# Date: 2026-07-24


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0
        curr = 0

        for i in nums:
            if i:
                curr += 1
            if not i:
                if curr >= mx:
                    mx = curr
                curr = 0
        
        if curr >= mx:
            return curr
        
        return mx
