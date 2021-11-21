class Solution:

    def floorSqrt(self,x): 
      
        if (x == 0 or x == 1): 
            return x 
      
        start = 1
        end = x
        res = 0
        
        while start <= end:
            mid = (start + end) // 2
            
            if mid*mid == x:
                return mid
            
            if mid*mid < x:
                start = mid+1
                res = mid
                
            else:
                end = mid-1
        
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
