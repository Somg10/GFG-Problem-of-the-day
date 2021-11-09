#User function Template for python3

#Back-end complete function Template for Python 3


class Solution:
    def dsum(self,n):
        s = 0
        while n > 0:
            s = s + (n%10)
            n = n // 10
        return s
            
    def RulingPair(self, arr, n): 
    	# Your code goes here
    	res = -1
    	mp = dict()
    	for i in range(n):
    	   nsm = self.dsum(arr[i])
    	   if nsm in mp:
    	       res = max(res,mp[nsm]+arr[i])
    	   mp[nsm] = max(mp.get(nsm, 0), arr[i])
    	return res
 
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution();
        print(obj.RulingPair(arr,n))



# } Driver Code Ends
