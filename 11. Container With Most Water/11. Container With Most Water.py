#
# Problem: 11. Container With Most Water
# Difficulty: Medium
# Link: https://leetcode.com/problems/container-with-most-water/description/
# Language: python3
# Date: 2026-03-25


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ar = 0
        a, b = 0, n-1

        while a < b:
            area = min(height[a],height[b])*(b-a)
            ar = max(ar,area)
            if height[a]<height[b]:
                a+=1
            else:
                b-=1
        return ar
