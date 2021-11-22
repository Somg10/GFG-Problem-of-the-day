#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    #code here
	    if n == 0 or n == 1 :
	        return 0
	    dz = False 
	    if arr[0] == 0 :
	        return -1
	    mx = arr[0]
	    stp = arr[0]
	    jmp = 0
	    for i in range (1,n-1):
	        stp = stp - 1
	        mx = max(mx,arr[i]+i)
	        if stp == 0:
	            jmp = jmp + 1
	            stp = mx - i
	            if stp <= 0:
	                return -1
	    return jmp+1
	    
	   
	    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends
