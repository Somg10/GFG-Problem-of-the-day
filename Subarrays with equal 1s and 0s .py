#User function Template for python3

class Solution:
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        mp={}
        curr_sum=0
        count=0
        for i in range(n):
            if arr[i]==0:
                curr_sum+=-1
            else:
                curr_sum+=arr[i]
            mp[curr_sum]=mp.get(curr_sum,0)+1
        for key,value in mp.items():
            
            if value>1:
                count+=(value*(value-1))//2
        if 0 in mp.keys():
            count+=mp[0]
        return count
    
    
    
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        obj = Solution()
        print(obj.countSubarrWithEqualZeroAndOne(arr, n))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
