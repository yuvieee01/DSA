#
# Problem: 81. Search in Rotated Sorted Array II
# Difficulty: Medium
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# Language: python3
# Date: 2026-09-12


# Optimal
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
                
            # The Duplicate Blind Spot
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                
            # Left half is strictly sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # Right half is strictly sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False
