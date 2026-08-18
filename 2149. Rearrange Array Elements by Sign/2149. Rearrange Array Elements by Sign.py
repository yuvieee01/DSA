#
# Problem: 2149. Rearrange Array Elements by Sign
# Difficulty: Medium
# Link: https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
# Language: python3
# Date: 2026-08-18


# Optimal Approach:
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pos = 0
        neg = 1

        for num in nums:
            if num > 0:
                res[pos] = num
                pos += 2

            elif num < 0:
                res[neg] = num
                neg += 2
        
        return res


''' # Brute:
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        pos = []
        neg = []

        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        
        for i in range(len(nums)//2):
            res.append(pos[i])
            res.append(neg[i])
        
        return res
'''
