#User function Template for python3

class Solution:
    def solve(self, arr, n):
        # code here
        arr.sort()
        a ='0'
        b ='0'
        for i in range(0,n-1,2):
            a+=str(arr[i])
            b+=str(arr[i+1])
        if n%2:
            a+=str(arr[-1])
        return int(''.join(b))+int(''.join(a))

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.solve(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
