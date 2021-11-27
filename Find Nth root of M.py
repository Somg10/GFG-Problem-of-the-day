#User function Template for python3

class Solution:
	def NthRoot(self, n, m):
		# Code here
		if m == 1:
		    return 1
		for i in range(2,m+1):
		    temp = int(pow(i,n))
		    if temp == m :
		        return i
		    if temp > m :
		        return -1
		return -1
		    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		ob = Solution()
		ans = ob.NthRoot(n, m)
		print(ans)
# } Driver Code Ends
