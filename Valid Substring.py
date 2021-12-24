#User function Template for python3

class Solution:
    def findMaxLen(ob, S):
        # code here 
        s = [-1]
        result = 0
        for i in range(0,len(S)):
            if S[i]=='(':
                s.append(i)
            else :
                s.pop()
                if s !=[]:
                    result = max(result,i-s[-1])
                else :
                    s.append(i)
        return result
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        print(ob.findMaxLen(S))
# } Driver Code Ends
