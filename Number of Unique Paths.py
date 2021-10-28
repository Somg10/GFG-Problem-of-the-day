#User function Template for python3
import numpy as np   
class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self,a, b):
        #code here
        dp = np.zeros([a,b],dtype=int)
        for i in range(a):
            for j in range(b):
                if i==0 or j==0:
                    dp[i][j]=1
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[a-1][b-1]    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a_b = [int(x) for x in input().strip().split()]
        a = a_b[0]
        b = a_b[1]
        ob = Solution()
        print(ob.NumberOfPaths(a, b))

# } Driver Code Ends
