#User function Template for python3

class Solution:
    
    #Function to count paths between two vertices in a directed graph.
    def countPaths(self, V, adj, source, destination):
        # code here
        if source==destination: return 1
        return sum([self.countPaths(V, adj, child, destination) for child in adj[source]])

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
		source, destination = map(int, input().split())
		ob = Solution()
		print(ob.countPaths(V, adj,source,destination))
        

# } Driver Code Ends
