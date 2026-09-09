#
# Problem: 1539. Kth Missing Positive Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/kth-missing-positive-number/
# Language: python3
# Date: 2026-09-09


class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        count = 1
        i = 0

        while k > 0:

            if i < len(arr) and arr[i] == count:
                i += 1      # Move to the next array element
            else:
                k -= 1      # The number is missing! Countdown k.
                
            # If k hits 0, this current count is our answer
            if k == 0:
                return count
                
            # Always increment the number we are checking
            count += 1
            
        return count
