# You are required to complete this fucntion
# Function should return an integer
class Solution:
    def findK(self, a, n, m, k):
        # Your code goes here
        t = 0
        l = 0
        r = m-1;
        b = n-1;
        dir =0;
        count=0;
        while(t<=b and l<=r):
            if(dir==0):
                for i in range(l, r+1):
                    k -= 1
                    if k == 0:
                        return (a[t][i])
                t += 1
                dir=1
                    
            if(dir==1):
                for i in range(t, b+1):
                    k -= 1
                    if k == 0:
                        return (a[i][r])
                r -= 1
                dir=2
            if(dir==2):
                for i in range(r, l - 1, -1):
                    k -= 1
                    if k == 0:
                        return (a[b][i])
                b -= 1
                dir=3
            if(dir==3):
                for i in range(b, t - 1, -1):
                    k -= 1
                    if k == 0:
                        return (a[i][l])
                l += 1
                dir=0



#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c+=1
        obj = Solution()
        print(obj.findK(matrix, n[0], n[1], n[2]))

# } Driver Code Ends
