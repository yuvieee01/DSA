#
# Problem: 34. Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Language: python3
# Date: 2026-09-11


# Brute:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        frst = -1
        lst = -1

        for i in range(len(nums)):
            if nums[i] > target:
                break
            if frst == -1 and nums[i] == target:
                frst = i
            if nums[i] == target:
                lst = i
        
        return [frst, lst]
