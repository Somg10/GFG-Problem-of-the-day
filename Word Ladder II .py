import collections
class Solution:
    def findSequences(self, beginWord, endWord, wordList):
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList: return []
        found, q, nq = False, {beginWord}, set()
        while q and not found:
            words -= set(q)
            for x in q:
                for y in [x[:i]+c+x[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                    if y in words:
                        if y == endWord: 
                            found = True
                        else: 
                            nq.add(y)
                        tree[x].add(y)
            q, nq = nq, set()
        return self.solve(beginWord,endWord, tree)
    def solve(self,x,endWord, tree):
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in self.solve(y,endWord,tree)]

#{ 
#  Driver Code Starts
from collections import deque 
import functools

def comp(a, b):
    x = ""
    y = ""
    for i in a:
        x += i 
    for i in b:
        y += i
    if x>y:
        return 1
    elif y>x:
        return -1 
    else:
        return 0

if __name__ == '__main__':
    T=int(input())
    for tt in range(T):
        n = int(input())
        wordList = []
        for i in range(n):
            wordList.append(input().strip())
        startWord = input().strip()
        targetWord = input().strip()
        obj = Solution()
        ans = obj.findSequences(startWord, targetWord, wordList)
        if len(ans)==0:
            print(-1)
        else:
            ans = sorted(ans, key=functools.cmp_to_key(comp))
            for i in range(len(ans)):
                for j in range(len(ans[i])):
                    print(ans[i][j],end=" ")
                print()

# } Driver Code Ends
