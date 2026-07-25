class Solution:
    def isPalinArray(self, arr):
        for i in arr:
            i = str(i)
            if i != i[::-1]:
                return False
        
        return True