#User function Template for python3

class Solution:
    def minTime(self, dependency, duration, n, m):
        #code here
        indeg=[0]*n
        ans=[]
        q=[]
        dp=[]
        adj=[]
        for i in range(n):
            adj.append([])
            dp.append(duration[i])
           
        for i in range(m):
            indeg[dependency[i][1]]+=1
            adj[dependency[i][0]].append(dependency[i][1])
        for i in range(n):
            if(indeg[i]==0):
                q.append(i)
        while(q):
            a=q.pop(0)
            ans.append(a)
            for i in adj[a]:
                dp[i]=max(dp[i],duration[i]+dp[a])
                indeg[i]-=1
                if(indeg[i]==0):
                    q.append(i)
                   
        if(len(ans)!=n):
            return -1
        return max(dp)

#{ 
#  Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    n,m= map(int,input().split())
    duration = list(map(int,input().split()))
    dependency = []
    for i in range(0,m):
        l = list(map(int,input().split()))
        dependency.append(l)
    obj = Solution()
    print(obj.minTime(dependency,duration,n,m))
# } Driver Code Ends
