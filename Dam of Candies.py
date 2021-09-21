class Solution:
    def maxCandy(self, height, n): 
        # Your code goes here
            f = 1
            l = n-1
            x = 0
            while f<l:
                b = l - f
                m = min(height[f-1], height[l])
                x = max(x, b*m)
                if height[l]>height[f-1]:
                    f+=1
                elif height[l]<height[f-1]:
                    l-=1
                else:
                    l-=1
            return x
