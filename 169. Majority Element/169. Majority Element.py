#
# Problem: 169. Majority Element
# Difficulty: Easy
# Link: https://leetcode.com/problems/majority-element/submissions/2100609184/
# Language: python3
# Date: 2026-08-10


# Optimal Approach
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate


''' # Better Approach:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        target = len(nums) // 2
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1    # Add 1 to the current count (or 0 if it doesn't exist yet)

            if freq[num] > target:
                return num

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
'''
