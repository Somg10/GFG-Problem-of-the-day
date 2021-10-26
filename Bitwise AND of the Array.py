#User function Template for python3
class Solution:
    def count(self, N, A, X): 
        # code here
        p=0
        ans=N
        for i in range(30,-1,-1):
            if ((X>>i)&1)!=0:
                p^=(2**i)
                continue
            c=0
            pr=p^(2**i)
            for j in A:
                if (j&pr)==pr:
                    c+=1
            ans=min(ans,N-c)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(N, A, X)
        print(ans)
# } Driver Code Ends
