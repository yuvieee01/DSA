#
# Problem: 1464. Maximum Product of Two Elements in an Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/submissions/2093148626/
# Language: python3
# Date: 2026-08-03


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = float('-inf')
        max2 = float('-inf')

        for num in nums:
            if num > max1:
                max2 = max1     # If we find a new biggest number, the old biggest gets demoted to second place
                max1 = num

            elif num > max2:
                max2 = num
        
        return (max1 - 1) * (max2 - 1)

'''
# What I did: TC - O(N log N)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()     # Sorts the list in-place
        return ((nums[-1]-1)*(nums[-2]-1))
'''
