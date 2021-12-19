#User function Template for python3

class Solution:
    def encryptString(self, S):
        # code here
        ans=""
        count=0
        c=S[0]
        count=1
        for i in range(1,len(S)):
            if S[i]==S[i-1]:
                count+=1
            else:
                ans+=c
                hx=""
                while(count):
                    rem=count%16
                    if(rem<10):
                        hx+=chr(48+rem)
                    else:
                        hx+=chr(97+rem-10) 
                    count//=16 
                ans+=hx 
                c=S[i]
                count=1
                
        ans+=c 
        hx=""
        while(count):
            rem=count%16
            if(rem<10):
                hx+=chr(48+rem)
            else:
                hx+=chr(97+rem-10) 
            count//=16 
        ans+=hx
        ans=ans[::-1]
        
        return ans

#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        print(ob.encryptString(S))
# } Driver Code Ends
