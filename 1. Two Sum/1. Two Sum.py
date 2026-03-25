#
# Problem: 1. Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/description/
# Language: python3
# Date: 2026-03-25


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            rem = target-nums[i]
            if rem in dic:
                return [dic[rem], i]
            dic[nums[i]] = i
            
