#
# Problem: 75. Sort Colors
# Difficulty: Medium
# Link: https://leetcode.com/problems/sort-colors/submissions/2080783707/
# Language: python3
# Date: 2026-07-25


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        a, b, c = 0, 0, n-1

        while b <= c:
            if nums[b] == 0:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b += 1
            
            elif nums[b] == 2:
                nums[c] , nums[b] = nums[b], nums[c]
                c -= 1
            
            else:
                b += 1
