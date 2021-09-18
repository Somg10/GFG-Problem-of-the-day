class Solution:
    def querySum(self, n, arr, q, queries):
        # code here
        arr1= [0] + arr
        for i in range (1,n+1):
            arr1[i] += arr1[i-1]
        r=[]
        for i in range(0,2*q-1,2):
            r.append(arr1[queries[i+1]] - arr1[queries[i]-1])
        return r
