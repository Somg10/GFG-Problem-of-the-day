import heapq
class Solution:
    def smallestRange(self, num, n, k):
        mh=[]
        mx=-float('inf')
        for i in range(k):
            heapq.heappush(mh,(num[i][0],i,0))
            mx=max(num[i][0],mx)
        heapq.heapify(mh)
        d=mx-mh[0][0]
        ans=[mh[0][0],mx]
        
        while True:
            mini,r,c=heapq.heappop(mh)
            if d>mx-mini:
                d=mx-mini
                ans=[mini,mx]
            if c+1>=len(num[r]):
                break
            nb=num[r][c+1]
            mx=max(mx,nb)
            heapq.heappush(mh,(nb,r,c+1))
        return ans
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    line=input().strip().split()
    n=int(line[0])
    k=int(line[1])
    numbers=[]
    for i in range(k):
        numbers.append([int(x) for x in input().strip().split()])
    r = Solution().smallestRange(numbers, n, k)
    print(r[0],r[1])
# } Driver Code Ends
