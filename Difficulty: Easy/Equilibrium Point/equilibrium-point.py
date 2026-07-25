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