class Solution:
		# Code here
	def dc(self,s,t,p1,p2):
        if p1 == 0:
            return p2
        if p2 == 0:
            return p1
        
        if self.dp[p1][p2] != -1:
            return self.dp[p1][p2]
        
        if s[p1-1 ] == t[p2-1] :
            self.dp[p1][p2] = self.dc(s,t,p1-1,p2-1)
            return self.dp[p1][p2]
            
        self.dp[p1][p2] = min(1+self.dc(s,t,p1,p2-1) ,1+self.dc(s,t,p1-1,p2))
        self.dp[p1][p2] = min(self.dp[p1][p2],1+self.dc(s,t,p1-1,p2-1))
        return self.dp[p1][p2]
    
    def editDistance(self, s, t):
        
        self.dp = [[-1 for i in range(len(t)+1)] for i in range(len(s)+1)]
        
        return self.dc(s,t,len(s),len(t))

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends
