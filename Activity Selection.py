#User function Template for python3
from functools import cmp_to_key
class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def compare(self,a,b) :
        if a[0][1]!=b[0][1] :
            return a[0][1]-b[0][1]
        return a[1]-b[1]
        
    def activitySelection(self,n,start,end):
        
        # code here
        x = []
        for i in range(n):
            x.append([[start[i],end[i]],i+1])
        
        x = sorted(x, key=cmp_to_key(self.compare))
        l = 0
        c = 0
        
        for i in range(n) :
            if x[i][0][0] > l :
                c += 1
                l = x[i][0][1]
    
        return c

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.activitySelection(n,start,end))
# } Driver Code Ends
