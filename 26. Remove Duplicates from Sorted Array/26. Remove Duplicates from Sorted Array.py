#
# Problem: 26. Remove Duplicates from Sorted Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# Language: python3
# Date: 2026-08-22


class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 0

        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1

