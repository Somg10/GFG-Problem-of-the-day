#Your task is to complete this Function \

class Solution:
    #function should return True/False
    def isInterleave(self, A, B, C):
        # Code here
        al=len(A)
        bl=len(B)
        cl=len(C)
        if cl != al+bl:
            return False
        
        p = [[None for i in range(bl+1)] for i in range(al+1)]
        p[0][0]= True
        for i in range(1, al+1):
            p[i][0] = p[i-1][0] and (A[i-1]==C[i-1])
            
        for j in range(1, bl+1):
            p[0][j] = p[0][j-1] and (B[j-1]==C[j-1])
            
        for i in range(1,al+1):
            for j in range(1,bl+1):
                x=p[i-1][j] and (A[i-1]==C[i+j-1])
                y=p[i][j-1] and (B[j-1]==C[i+j-1])
               
                p[i][j]=(x or y)
        
        return p[-1][-1]    


#{ 
#  Driver Code Starts
#Initial template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr=input().strip().split()
        if Solution().isInterleave(arr[0], arr[1], arr[2]):
            print(1)
        else:
            print(0)

# } Driver Code Ends
