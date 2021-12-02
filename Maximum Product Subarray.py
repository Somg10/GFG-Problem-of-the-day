#User function Template for python3
import sys
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
	    minn,maxx = 1,1
	    ans = -sys.maxsize-1
	    for i in range(0,n):
	        if(arr[i] == 0):
	            ans = max(ans,0)
	            minn = 1
	            maxx = 1
	            continue
	       
	        elif(arr[i]>0):
	            minn = min(arr[i],minn*arr[i])
	            maxx = max(arr[i],maxx*arr[i])
	       
	        else:
	            new_minn = maxx*arr[i]
	            new_maxx = minn*arr[i]
	            minn = min(arr[i],new_minn)
	            maxx = max(arr[i],new_maxx)
	        
	        ans = max(ans,maxx)
	   
	    return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
