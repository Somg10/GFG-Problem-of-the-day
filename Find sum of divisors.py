#User function Template for python3

class Solution:
    def sumOfDivisors(self, N):
    	#code here 
    	s = 0
    	for i in range(1,N+1):
    	    if N%i == 0:
    	        for j in range (1,i+1):
    	            if i%j == 0:
    	                s = s+j
    	return s

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
# } Driver Code Ends
