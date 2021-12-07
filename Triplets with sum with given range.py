#User function Template for python3
class Solution:
    def count(self,arr, n, v):
        arr.sort()
        ans = 0
        j = 0
        k = 0
        s = 0
        for i in range(0,n-2):
            j = i+1
            k = n-1
            while j!=k :
                s = arr[i]+arr[j]+arr[k]
                if s>v:
                    k-=1
                else :
                    ans+=(k-j)
                    j+=1
        return ans
        
    def countTriplets(self,arr, n, a, b):
        res = 0
        res = (self.count(arr, n, b)-self.count(arr, n, a-1))
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        L,R = input().split()
        L=int(L)
        R=int(R)
        ob = Solution()
        print(ob.countTriplets(Arr, N, L, R))
# } Driver Code Ends
