#User function Template for python3
class Solution:
    def search(self,pat, txt):
        lt = len(txt) 
        lp = len(pat) 
        ans = 0
        ar = [0]*26 
        br = [0]*26
    
        for i in range(lp):
            ar[ord(pat[i]) - 97] += 1
            br[ord(txt[i]) - 97] += 1
    
        for i in range(lp, lt):
            if ar == br:
                ans += 1
            br[ord(txt[i]) - 97] += 1
            br[ord(txt[i-lp]) - 97] -= 1
        if ar == br:
            return ans+1
        else:
            return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends
