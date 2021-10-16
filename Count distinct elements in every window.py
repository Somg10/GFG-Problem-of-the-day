from collections import defaultdict 
class Solution:
    def countDistinct(self, A, n, k):
    	mp = defaultdict(lambda:0)
    	dist_count = 0
    	for i in range(k): 
    		if mp[A[i]] == 0: 
    			dist_count += 1
    		mp[A[i]] += 1
    		
    	res = []
    	res.append (dist_count)
    	for i in range(k, n):
    		if mp[A[i - k]] == 1: 
    			dist_count -= 1
    		mp[A[i - k]] -=1
    		if mp[A[i]] == 0: 
    			dist_count += 1
    		mp[A[i]] += 1
    		res.append (dist_count)
    		
    	return res

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends
