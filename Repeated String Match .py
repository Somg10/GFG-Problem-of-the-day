class Solution:
    def repeatedStringMatch(self, A, B):
        # code here
        NA =A
        r=1
        while len(NA)<len(B):
            NA+=A
            r+=1
        if B in NA:
            return r
        if B in NA+A:
            return r+1
        return -1
