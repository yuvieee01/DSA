#
# Problem: 283. Move Zeroes
# Difficulty: Easy
# Link: https://leetcode.com/problems/move-zeroes/description/
# Language: python3
# Date: 2026-07-25


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0

        for s in range(len(nums)):
            if nums[s] != 0:
                nums[s], nums[a] = nums[a], nums[s]
                a += 1
