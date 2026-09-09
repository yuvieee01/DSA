#
# Problem: 35. Search Insert Position
# Difficulty: Easy
# Link: https://leetcode.com/problems/search-insert-position/
# Language: python3
# Date: 2026-09-09


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # This is a binary search question. O(log N)

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid

        return l

