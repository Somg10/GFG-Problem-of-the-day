#User function Template for python3

# Function to calculate average
def calc_average(arr):
    # Your code here
    a = min(arr)
    b = max(arr)
    add = sum(arr)
    n = len(arr)
    add= add-(a+b)
    s = add//(n-2)
    return s
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


# Driver Code
if __name__ == '__main__':
    # Testcase input
    testcases = int(input())
    # Looping through testcases
    while(testcases > 0):
        N = int(input())
        
        a = list(map(int,input().strip().split()))
        
        print (calc_average(a))
        
        testcases -= 1
# } Driver Code Ends
