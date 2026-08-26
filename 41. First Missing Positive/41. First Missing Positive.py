#
# Problem: 41. First Missing Positive
# Difficulty: Hard
# Link: https://leetcode.com/problems/first-missing-positive/description/
# Language: python3
# Date: 2026-08-26


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Cyclic Sort to put valid numbers in their correct index
        for i in range(n):
            # Keep swapping while the number is in the valid range [1, n] 
            # and it is not already sitting in its correct room
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Store the target index to avoid Python's tuple assignment evaluation bug
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Step 2: Scan to find the first index that doesn't match its room number
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # Step 3: If everything is perfectly in order (e.g., [1, 2, 3])
        return n + 1
