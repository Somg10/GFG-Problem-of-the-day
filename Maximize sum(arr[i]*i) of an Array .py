#User function Template for python3

class Solution:
    def Maximize(self, a, n): 
        # Complete the function
        
        arr.sort()
        res = 0
        high = 1000000007
        for i in range(n):
            res = res + (i*arr[i])
            
        return res%high
            
      


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    print(ob.Maximize(arr, n))
    
# } Driver Code Ends
