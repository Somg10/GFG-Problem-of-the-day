class Solution:
	def overlappedInterval(self,v):
		#Code here
		v.sort()
		l = len(v)
		if l <= 1:
		    return v
 
        st=v[0][0]
        ed=v[0][1]
 
        res=[]
        for i in range(1,l):
            if v[i][0]<=ed:
                ed=max(ed,v[i][1])
            else:
                res.append([st,ed])
                st=v[i][0]
                ed=v[i][1]
        res.append([st,ed])        
        return res        
#{ 
#  Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends
