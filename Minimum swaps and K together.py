#User function Template for python3

def minSwap (arr, n, k) : 
    #Complete the function
    c1 = 0
    c2 = 0
    for i in range(n):
        if arr[i]<=k:
            c1 = c1 +1
    for i in range(c1):
        if arr[i]<=k:
            c2 = c2 +1
    res = c1 - c2
    for i in range(1,(n+1-c1)):
        if arr[i-1] <= k:
            c2 = c2 -1
        if arr[i+c1-1] <= k:
            c2 = c2 +1
        res = min(res,c1-c2)
    return res
            
    
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ans = minSwap(arr, n, k)
    print(ans)
    





# } Driver Code Ends
