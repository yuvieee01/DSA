class Solution:
    def getSecondLargest(self, arr):
        mx = -1
        res = -1
        
        for i in arr:
            if i > mx:
                res = mx
                mx = i
            if i > res and i < mx:
                res = i

        return res