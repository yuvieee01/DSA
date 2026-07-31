#
# Problem: 169. Majority Element
# Difficulty: Easy
# Link: https://leetcode.com/problems/majority-element/
# Language: python3
# Date: 2026-07-31


# Brute:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            c = 0
            for i in nums:
                if num == i:
                    c += 1
                    if c > len(nums)//2:
                        return num
