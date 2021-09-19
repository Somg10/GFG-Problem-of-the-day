class Solution:
    def MedianOfArrays(self, array1, array2):
            #code here
            l = len(array1)+len(array2)
            arr=[]
            
            arr =  array1+array2
            arr.sort()
            mid = l // 2
            if l%2 == 0:
               res=(arr[mid]+arr[(mid)-1])
               
               if res%2 == 0:
                   return res//2
               return res/2    
               
            else:
                 res=arr[mid]
            return res
            
        
#{ 
#  Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends
