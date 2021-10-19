#User function Template for python3


class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,histogram):
        #code here
        s = list()
        ma = 0
        i = 0
        while i < len(histogram):
            if (not s) or (histogram[s[-1]] <= histogram[i]):
                s.append(i)
                i += 1
            else:
                ts = s.pop()
                ar = (histogram[ts] *
                        ((i - s[-1] - 1)
                         if s else i))
                ma = max(ma,ar)
        while s:
            ts = s.pop()
            ar = (histogram[ts] * ((i - s[-1] - 1) if s else i))
            ma = max(ma, ar)
        return ma

#{ 


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends
