#
# Problem: 189. Rotate Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotate-array/
# Language: python3
# Date: 2026-07-27


# What I did (Pythonic Way):-
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n   # If k > length of nums
        while k != 0:
            temp = nums[-1]
            for i in range(n-2, -1, -1):
                nums[i+1] = nums[i]
            nums[0] = temp
            k -= 1
