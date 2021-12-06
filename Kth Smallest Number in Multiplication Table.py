class Solution(object):
    def findKthNumber(self, m, n, k):
        #Write your code here
        low = 1
        high = m*n
        while low <= high:
            count = 0
            mid = (low+high)//2
            for i in range(1,m+1):
                count = count + min(mid//i,n)
            if count >= k:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    arr = list(map(int, input().split())) 
    ob = Solution()
    print(ob.findKthNumber(arr[0],arr[1], arr[2]))
# } Driver Code Ends
