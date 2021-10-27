#User function Template for python3

class Solution:

    def convert(self, Str, n):
        # code here
        if n == 1:
            return Str
        temp = ['']*n
        temp[0]+=Str[0]
        l = len(Str)
        i = 1
        j = 1
        flag = 1
        for k in range(1,l):
            if flag == 1:
                temp[i]+=Str[k]
                i+=1
                if i == n:
                    i = i-2
                    flag = 2
            elif flag == 2 and j < l :
                temp[i]+=Str[k]
                i-=1
                if i == -1:
                    i = i+2
                    flag = 1
            j+=1
        res = ''
        
        for x in temp:
            res+=x
        return res
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()
        n = int(input())

        solObj = Solution()

        print(solObj.convert(Str,n))
# } Driver Code Ends
