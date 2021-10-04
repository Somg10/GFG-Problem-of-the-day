#User function Template for python3
class Solution:
	def maxSubstring(self, S):
		# code here
		d1 = 0
		d2 = 0
		df = -1
		for i in S:
		    if i == '1':
		        d1 += 1
		    else:
		        d2 += 1
		    
		    if d1 > d2:
		        d1 = 0
		        d2 = 0
		    df = max(df, d2-d1)
		 
	    if df == 0:
	        return -1
	    return df
		        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.maxSubstring(s)
		print(answer)

# } Driver Code Ends
