#
# Problem: 53. Maximum Subarray
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-subarray/submissions/1959313975/
# Language: python3
# Date: 2026-03-25


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curr_sum = 0

        for i in nums:
            curr_sum += i
            ans = max(ans, curr_sum)

            if curr_sum < 0:
                curr_sum = 0
        
        return ans
