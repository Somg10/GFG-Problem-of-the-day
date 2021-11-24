class Solution:
    def trappingWater(self, arr,n):
        #Code here 
        lhigh = [0]*n
        rhigh = [0]*n
        w = 0
        lhigh[0] = arr[0] 
        for i in range( 1, n): 
            lhigh[i] = max(lhigh[i-1], arr[i])
        rhigh[n-1] = arr[n-1] 
        for i in range(n-2, -1, -1): 
            rhigh[i] = max(rhigh[i+1], arr[i]);
        for i in range(0, n): 
            w = w + min(lhigh[i],rhigh[i]) - arr[i]
        return w 
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends
