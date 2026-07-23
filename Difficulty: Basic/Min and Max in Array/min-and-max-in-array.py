class Solution:
    def getMinMax(self, arr):

        # return [min(arr), max(arr)]
        
        n = len(arr)
        
        if n == 0:
            return -1
        
        if n == 1:
            return [arr[0], arr[0]]
        
        if arr[0] <= arr[1]:
            min = arr[0]
            max = arr[1]
        else:
            max = arr[0]
            min = arr[1]
        
        for i in arr:
            if i >= max:
                max = i 
            if i <= min:
                min = i

        return [min, max]