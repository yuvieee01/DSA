class Solution:
    def findEquilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0
        
        for i in range(len(arr)):
            # Right sum is total sum minus what's on the left, minus the current element
            right_sum = total_sum - left_sum - arr[i]
            
            # Check for equilibrium
            if left_sum == right_sum:
                return i
                
            # Add current element to left_sum for the next iteration
            left_sum += arr[i]
            
        return -1

""" What I did actually:
class Solution:
    def findEquilibrium(self, arr):
        n = len(arr)
        s = sum(arr)
        temp = 0
        
        for i in range(n):
            temp += arr[i]
            l = temp - arr[i]
            r = s - temp
            if l == r:
                return i
        
        return -1
"""
