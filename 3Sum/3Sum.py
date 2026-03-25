#
# Problem: 3Sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/3sum/submissions/1959321261/
# Language: python3
# Date: 2026-03-25


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            l, r = i + 1, n - 1
            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif t < 0:
                    l += 1
                else:
                    r -= 1
        return res
