#User function Template for python3

class Solution:
    def reverseWords(self, s):
        # code here
        nstr = s.split('.')
        tmp = ''
        for i in nstr:
            tmp += i[::-1]
            tmp += '.'
        return tmp[:-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseWords(s)
        print(ans)
# } Driver Code Ends
