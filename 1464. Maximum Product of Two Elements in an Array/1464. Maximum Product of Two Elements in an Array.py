#
# Problem: 1464. Maximum Product of Two Elements in an Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/submissions/2093139931/
# Language: python3
# Date: 2026-08-03


# What I did: TC - O(N log N)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()     # Sorts the list in-place
        return ((nums[-1]-1)*(nums[-2]-1))
