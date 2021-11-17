#{ 
#Driver Code Starts
#Initial Template for Python 3

import heapq

 # } Driver Code Ends
#User function Template for python3

class Solution:
    def Kclosest(self, arr, n, x, k):
        # Your code goes here
        mheap = [ ( -1*abs(x-arr[i]) , -1*arr[i] ) for i in range(k) ]
        heapq.heapify(mheap) 
        for i in range(k,n):
            dist = -1*mheap[0][0]
            nub  = -1*mheap[0][1]
            if abs(arr[i]-x)<dist or ( abs(arr[i]-x)==dist and arr[i]<nub ):
                heapq.heappop(mheap)
                heapq.heappush( mheap, ( -1*abs(x-arr[i]) , -1*arr[i] ) )
        
        res=[ -1*x[1] for x in mheap]
        res.sort()
        return res


#{ 
#Driver Code Starts.
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int( line[0] )
        x=int( line[1] )
        k=int( line[2] )
        arr=[int(x) for x in input().strip().split()]
        obj = Solution()
        result=obj.Kclosest(arr, n, x, k)
        for i in result:
            print(i, end=' ')
        print()
#} Driver Code Ends
