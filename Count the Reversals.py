import math
def countRev (s):
    # your code here
    c = 0
    r = 0
    for i in s:
        if i == '{':
            c = c+1
        else:
            if c == 0:
                r = r + 1
                c = c+1
            else:
                c = c-1
    if c % 2: 
        return '-1'
    r = r + (c//2)
    return r

        

#{ 
#  Driver Code Starts

t = int (input ())
for tc in range (t):
    s = input ()
    print (countRev (s))



# } Driver Code Ends
