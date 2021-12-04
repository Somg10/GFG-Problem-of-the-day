#User function Template for python3

class Solution:
    def getLastDigit(self, a, b):
        # code here 
        if b == "0":
            return 1
        a = int(a[-1])
        b = int(b[-2:])
        if a in (0, 1, 5, 6):
            return a
        if a not in (4, 9):
            if b & 1:
                a = 10 - a
            else:
                a = 4 if a in(2, 8) else 9
            b>>=1
        return a if b & 1 else 10 - a
                
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b=map(str,input().split())
        
        ob = Solution()
        print(ob.getLastDigit(a,b))
# } Driver Code Ends
