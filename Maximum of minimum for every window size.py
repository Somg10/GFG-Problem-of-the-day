#Back-end complete function Template for Python 3

class Solution:
    
    #Function to find maximum of minimums of every window size.
    def maxOfMin(self,arr,n):
        # code here
        s = []  
        l = [-1 for i in range(n)]
        r = [n for i in range(n)] 
        for i in range(n):
            while len(s) and arr[s[-1]]>=arr[i]:
                s.pop()
            if len(s):
                l[i] = s[-1]
            s.append(i)
        s = []
        for i in range(n-1,-1,-1):
            while len(s) and arr[s[-1]]>=arr[i]:
                s.pop()
            if len(s):
                r[i] = s[-1]
            s.append(i)
        res= [0 for i in range(n+1)]
        for i in range(n):
            length = r[i]-l[i]-1
            res[length] = max(res[length],arr[i])
        for i in range(n-1,-1,-1):
            res[i] = max(res[i],res[i+1])
        return res[1:]

        
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys



_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.maxOfMin(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()

# } Driver Code Ends
