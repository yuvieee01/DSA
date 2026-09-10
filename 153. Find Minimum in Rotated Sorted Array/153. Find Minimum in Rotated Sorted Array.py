#
# Problem: 153. Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# Language: python3
# Date: 2026-09-10


class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        return nums[l]
