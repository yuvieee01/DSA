#
# Problem: 485. Max Consecutive Ones
# Difficulty: Easy
# Link: https://leetcode.com/problems/max-consecutive-ones/description/
# Language: python3
# Date: 2026-08-22


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0
        curr = 0

        for num in nums:

            if num == 1:
                curr += 1
                mx = max(mx, curr)

            else:
                curr = 0

        return mx
