#User function Template for python3
import bisect #Use for Bisect Algorithm Functions 
class Solution:
    def ValidPair(self, a, n): 
    	# Your code goes here
    	a.sort()
    	res = 0
    	for i in range(n-1):
    	    if a[i]>0:
    	        k=(n-i)-1
    	        res += k*(k+1)//2
    	        return res
    	    nw = bisect.bisect_left(a,1-a[i])
    	    if nw<n:
    	        res += n-nw
    	        
    	return res
    	   
    	   

#{ 
#Driver Code Starts.

if __name__ == '__main__': 
	t = int(input())
	for _ in range(t):
		n = int(input())
		array = list(map(int, input().strip().split()))
		obj = Solution()
		ans = obj.ValidPair(array, n)
		print(ans) 



#} Driver Code Ends
