#
# Problem: 198. House Robber
# Difficulty: Medium
# Link: https://leetcode.com/problems/house-robber/
# Language: python3
# Date: 2026-05-12


'''
class Solution:
    def calc(self, idx, nums):
        if idx >= len(nums):
            return 0
        inc = nums[idx] + self.calc(idx + 2, nums)
        exc = self.calc(idx + 1, nums)

        return max(inc, exc)

    def rob(self, nums: List[int]) -> int:
        return self.calc(0, nums)

from functools import cache
'''

class Solution:
    # Use @cache to remember results of (idx) and prevent TLE
    @cache
    def calc(self, idx, nums_tuple):
        # Base case
        if idx >= len(nums_tuple):
            return 0

        # Recursive steps using self.calc
        # We 'include' the current house and skip one
        inc = nums_tuple[idx] + self.calc(idx + 2, nums_tuple)
        
        # We 'exclude' the current house and move to the next
        exc = self.calc(idx + 1, nums_tuple)

        return max(inc, exc)

    def rob(self, nums: List[int]) -> int:
        # We convert nums to a tuple because lists are not 'hashable' 
        # and cannot be used with @cache
        return self.calc(0, tuple(nums))
