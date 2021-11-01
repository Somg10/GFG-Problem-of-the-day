#User function Template for python3

class Solution:
	def isCircularPrime(self, n):
		# Code here
		if n == 1:
		    return 0
		
		l = len(str(n))
		x = l
		while l>0:
		    for i in range (2,(n//2)+1):
		        if n%i == 0:
		            return 0
		    tmp = str(n)
		    
		    n = int (tmp[x-1:]+tmp[:x-1])
		    l-=1
		return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.isCircularPrime(n)
		print(ans)
# } Driver Code Ends
