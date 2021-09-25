#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        if sum(arr) == 0:
            return n
        l = 0
        s = 0
        a = {}
        for i in range(n):
            s += arr[i]
            
            if arr[i] == 0 and l == 0:
                l = 1
            if s == 0:
                l = i+1
            if s in a:
                l = max(l, i-a[s])
            else:
                a[s] = i
                
        return l
