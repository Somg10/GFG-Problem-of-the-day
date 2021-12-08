#User function Template for python3
import sys
class Solution:
    def closestToZero (self,arr, n):
        # your code here
        arr.sort()
        ans=sys.maxsize
        i=0
        j=n-1
        while(i<j):
            sumi=arr[i]+arr[j]
            if abs(ans)>abs(sumi):
                ans=sumi
            if abs(ans)==abs(sumi):
                ans=max(ans,sumi)
            if sumi<0:
                i+=1
            else:
                j-=1
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range(t):
    n = int (input ())
    arr = list(map(int, input().split()))
    ob = Solution()
    print (ob.closestToZero (arr, n))
# } Driver Code Ends
