class Solution:
    def getAlternates(self, arr):
        # Code here
        
        # return arr[::2]

        return [arr[i] for i in range(0,len(arr),2)]