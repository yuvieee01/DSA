#
# Problem: 189. Rotate Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotate-array/description/
# Language: python3
# Date: 2026-08-18


class Solution:
    def rev(self, arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        self.rev(nums, 0, n-1)
        self.rev(nums, 0, k-1)
        self.rev(nums, k, n-1)
        

"""
# What I did (Brute)
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

===========================================================

# What i optimised (The Better Approach (Extra Memory))
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        res = [0] * n   # Extra Memory

        for i in range(n):
            res[(i+k) % n] = nums[i]    # new index: (i+k)%n

        nums[:] = res
"""
