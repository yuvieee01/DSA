#
# Problem: 704. Binary Search
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-search/
# Language: python3
# Date: 2026-09-07


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        n = len(nums)
        l = 0
        r = n-1

        while l <= r:
            m = (l + r)//2

            if nums[m] == target:
                return m

            elif nums[m] < target:
                l = m+1

            else:
                r = m-1

        return -1
