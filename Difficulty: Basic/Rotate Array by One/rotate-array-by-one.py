class Solution:
    def rotate(self, arr):
        temp = arr[-1]
        arr.pop()
        arr.insert(0,temp)
        return arr