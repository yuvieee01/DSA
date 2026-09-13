#
# Problem: 540. Single Element in a Sorted Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/single-element-in-a-sorted-array/
# Language: python3
# Date: 2026-09-13


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            mid = (mid // 2) * 2    # mid -= mid % 2 OR mid = mid ^ 1
            
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            
            else:
                right = mid
            
        return nums[left]
