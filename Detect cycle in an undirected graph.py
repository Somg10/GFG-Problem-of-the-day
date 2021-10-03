class Solution:
    def isCycle(self, V, adj):
		a = [0]*V
		
		def dfs(crt, prt):
		    a[crt] = 1
		    
		    for i in adj[crt]:
		        if not a[i]:
		            if dfs(i, crt): return True
		        elif i != prt:
		            return True
		            
		    return False
		
		for i in range(V):
		    if not a[i]:
		        if dfs(i, -1): return True
		        
		return False
    
    #Function to detect cycle in an undirected graph.
	

#{ 
#  Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
