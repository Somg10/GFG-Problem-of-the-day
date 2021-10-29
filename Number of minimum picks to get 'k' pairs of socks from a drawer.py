#User function Template for python3


class Solution:
    def find_min(self, a, n, k):
        #Code Here
        tmp=0
        res=n
        for i in range(len(a)):
            if i<n and tmp<k:
                a[i]-=1
                while a[i]>=2:
                    tmp+=1
                    if tmp == k:
                        res+=1
                        break
                    a[i]-=2
                    res+=2
        
        for j in range(n):
            if j<n and tmp<k:
                if a[j]>0:
                    tmp+=1
                    res+=1
        if tmp == k:
            return res 
        else:
            return -1



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        k = int(input())
        obj = Solution()
        print(obj.find_min(a,n,k))

# } Driver Code Ends
