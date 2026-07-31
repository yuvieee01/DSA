#
# Problem: 2149. Rearrange Array Elements by Sign
# Difficulty: Medium
# Link: https://leetcode.com/problems/rearrange-array-elements-by-sign/
# Language: python3
# Date: 2026-07-31


# Brute:
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
