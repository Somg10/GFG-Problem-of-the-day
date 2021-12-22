#User function Template for python3

class Solution:
    def maximizeSum(self, a, n, k):
        # Your code goes here
        a.sort()
        for i in range(n):
            if a[i]>0 or k==0:
                break
            else:
                a[i]=abs(a[i])
                k-=1
        a.sort()
        if k>0 and k%2==0:
            return sum(a)
        elif (k>0 and k%2!=0):
            a[0]=-a[0]
            return sum(a)
        else:
            return sum(a)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.maximizeSum(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends
