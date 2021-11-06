#User function Template for python3

class Solution:
    def divide(self, a, b):
        
        #code here
        if b < 0:
            sign = -1
        else:
            sign = 1
        if a < 0:
            s = -1
        else:
            s = 1
        a = abs(a)
        b = abs(b)
        q = 0
        t = 0
        for i in range(31, -1, -1):
            if (t + (b << i) <= a):
                t += b << i
                q |= 1 << i
         
        return sign * q * s

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        inp = list(map(int,input().split())) 
        
        a=inp[0]
        b=inp[1]
        
        ob=Solution()
        
        print(ob.divide(a,b))
        
# } Driver Code Ends
