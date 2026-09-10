class Solution:
    def firstIndex(self, arr):
        # code here
        for i, num in enumerate(arr):
            if num == 1:
                return i
        
        return -1
