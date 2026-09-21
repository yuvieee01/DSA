class Solution:
    def search(self, arr, x):
        # code here
        for i, num in enumerate(arr):
            if num == x:
                return i
        
        return -1