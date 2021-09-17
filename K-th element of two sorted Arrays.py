import numpy as np
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        rest=[]
        rest = arr1 + arr2
        rest.sort()
        r = rest[k-1]
        return r
