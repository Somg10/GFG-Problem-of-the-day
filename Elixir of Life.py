#User function Template for python3

class Solution:
    def maxFrequency(self, S):
       # code here
       stng = ""
       cnt=0
       l = len(S)
       for i in S:
           stng += i
           if (stng==S[l-len(stng):]):
               break
       
       for i in range(l-len(stng)+1):
           if S[i:i+len(stng):]==stng:
               cnt+=1
       return cnt
   
        
     
#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        Str = input()
        obj = Solution()

        print(obj.maxFrequency(Str))

# } Driver Code Ends
