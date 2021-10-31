#User function Template for python3

class Solution:
    def maxSumPairWithDifferenceLessThanK(self, arr, N, K): 
        # Your code goes here 
        mx = 0
        n = N-1
        arr.sort()
        i=n
        while i > 0:
            if arr[i]-arr[i-1] < K:
                mx+=arr[i]+arr[i-1]
                i-=1
            i-=1
        return mx

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        arr = [int(x) for x in input().strip().split()]
        K = int(input())
        ob=Solution()
        print( ob.maxSumPairWithDifferenceLessThanK(arr, N, K) )

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
