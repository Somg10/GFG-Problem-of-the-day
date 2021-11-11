class Solution:
    def countSub(self, arr, n, x):
        st = 0
        end = 0
        sum = 0
        cnt = 0
        while end < n:
            sum += arr[end]
            while st <= end and sum > x:
                sum -= arr[st]
                st+=1
            cnt += (end - st + 1)
            end+=1
        return cnt
    def countSubarray(self, N, A, L, R):
        Rt = self.countSub(A, N, R)
        Lt = self.countSub(A, N, L - 1)
        return Rt - Lt

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,L,R = map(int,input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countSubarray(N, A, L, R)
        print(ans)

# } Driver Code Ends
